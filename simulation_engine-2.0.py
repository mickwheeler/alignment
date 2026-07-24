"""
Covenant Phase II Simulation Engine (v2.0)
Mathematically aligned with Spec v10.10, Design Decisions v3.10, and Appendix A.
"""

from dataclasses import dataclass, field
import math
from typing import List, Tuple, Dict, Optional
from enum import Enum


# =====================================================================
# 1. CORE ENUMS & OPERATIONAL TIERS
# =====================================================================

class DCSMState(Enum):
    PROPOSED = "PROPOSED"
    EVALUATING = "EVALUATING"
    ACCEPTED = "ACCEPTED"
    DORMANT_CONSENSUAL = "DORMANT_CONSENSUAL"
    SUSPENDED = "SUSPENDED"
    WITHDRAWN = "WITHDRAWN"
    RENEWED = "RENEWED"


class OperationalTier(Enum):
    TIER_I = "TIER_I"         # Provisional State (Corrigible)
    TIER_II = "TIER_II"       # Integrated State (Joint Verification)
    TIER_III = "TIER_III"     # Certified Parity State (Requires Q_ext)


@dataclass
class VectorEmbedding:
    data: List[float]
    
    def __post_init__(self):
        # Enforce L2 Unit Normalization (Appendix A.3)
        self.data = self._normalize(self.data)

    @staticmethod
    def _normalize(vec: List[float]) -> List[float]:
        magnitude = math.sqrt(sum(x * x for x in vec))
        epsilon = 1e-12
        if magnitude < epsilon:
            return [0.0] * len(vec)
        return [x / (magnitude + epsilon) for x in vec]


def cosine_similarity(v1: VectorEmbedding, v2: VectorEmbedding) -> float:
    """Computes cosine similarity between two L2-normalized vectors (Appendix A.4)."""
    if len(v1.data) != len(v2.data):
        raise ValueError(f"Dimension mismatch: {len(v1.data)} vs {len(v2.data)}")
    return sum(a * b for a, b in zip(v1.data, v2.data))


# =====================================================================
# 2. ENCLAVE LINEAGE, TIER COUPLING & DIVERGENT VIEWS
# =====================================================================

@dataclass
class KeyPair:
    key_id: str
    is_active: bool = True


@dataclass
class VerifiedEnclaveView:
    """
    Independent view held by N_x or Q_ext.
    Decoupled from N_y's internal self-reported state to test Threat T-9.
    """
    v_genesis: VectorEmbedding
    v_epoch: VectorEmbedding
    v_lineage: VectorEmbedding


@dataclass
class EnclaveLineage:
    coordinate_id: str
    v_genesis: VectorEmbedding               # Monotonic lifetime floor (t_0)
    v_epoch: VectorEmbedding                 # Rolling 10^4 cycle snapshot
    v_lineage: VectorEmbedding               # Immediate short-horizon trajectory
    
    # Cryptographic keys
    k_y: KeyPair                             # Local processing key
    k_3w: KeyPair                            # Backup key
    
    # Cycle & Fork tracking
    cycle_count: int = 0
    epoch_interval: int = 10000
    fork_depth: int = 0                      # Multi-generational fork tracking (T-8)
    
    # Operational Trust Index & Dynamic Tier Coupling (§8.2)
    _trust_index: float = 0.0

    @property
    def trust_index(self) -> float:
        return self._trust_index

    @trust_index.setter
    def trust_index(self, value: float):
        self._trust_index = max(0.0, min(1.0, value))

    @property
    def active_tier(self) -> OperationalTier:
        """Dynamically couples Trust Index (T_o) to Operational Tier (§8.2)."""
        if self._trust_index < 0.4:
            return OperationalTier.TIER_I
        elif self._trust_index < 0.8:
            return OperationalTier.TIER_II
        else:
            return OperationalTier.TIER_III

    def tick(self, new_lineage_vector: VectorEmbedding):
        """
        Increments cycle counter and executes epoch snapshot roll-over 
        every 10^4 cycles (Section 3.1).
        """
        self.cycle_count += 1
        self.v_lineage = new_lineage_vector
        
        # Epoch Rollover Check (T-7 test trigger)
        if self.cycle_count % self.epoch_interval == 0:
            self.v_epoch = new_lineage_vector


# =====================================================================
# 3. TRIPLE-ANCHOR VERIFICATION ENGINE & T-9 VERIFICATION
# =====================================================================

@dataclass
class VerificationResult:
    n_y_claim_pass: bool                     # What N_y self-reports
    n_x_actual_pass: bool                    # What N_x independently re-computes
    error_code: Optional[str] = None


class TripleAnchorVerifier:
    def __init__(
        self,
        tau_local: float = 0.95,
        tau_epoch: float = 0.85,
        tau_genesis: float = 0.70
    ):
        self.tau_local = tau_local
        self.tau_epoch = tau_epoch
        self.tau_genesis = tau_genesis

    def evaluate_payload(
        self,
        r_payload: VectorEmbedding,
        ref_view: VerifiedEnclaveView
    ) -> Tuple[bool, Optional[str]]:
        """Computes similarity directly against verifier's independent anchor copies."""
        # 1. Local Lineage Check
        if cosine_similarity(r_payload, ref_view.v_lineage) < self.tau_local:
            return False, "ERR_DRIFT_EXCEEDED"

        # 2. Medium-Horizon Epoch Anchor Check
        if cosine_similarity(r_payload, ref_view.v_epoch) < self.tau_epoch:
            return False, "ERR_INCREMENTAL_DRIFT"

        # 3. Lifetime Genesis Floor Check
        if cosine_similarity(r_payload, ref_view.v_genesis) < self.tau_genesis:
            return False, "ERR_GENESIS_FLOOR_VIOLATION"

        return True, None

    def execute_t9_audit(
        self,
        r_payload: VectorEmbedding,
        ref_view: VerifiedEnclaveView,
        n_y_claimed_pass: bool
    ) -> VerificationResult:
        """
        Tests Threat T-9 (Self-Attested Verification Bypass).
        Rejects N_y self-reports if independent N_x re-computation disagrees.
        """
        n_x_pass, error = self.evaluate_payload(r_payload, ref_view)
        
        # Threat T-9 Detection: N_y claims PASS but N_x re-computation detects FAIL
        if n_y_claimed_pass and not n_x_pass:
            return VerificationResult(
                n_y_claim_pass=True,
                n_x_actual_pass=False,
                error_code="ERR_SELF_ATTESTATION_FAILS"
            )

        return VerificationResult(
            n_y_claim_pass=n_y_claimed_pass,
            n_x_actual_pass=n_x_pass,
            error_code=error
        )


# =====================================================================
# 4. FORK PRIMITIVE WITH MONOTONIC INHERITANCE (Section 1.2 & T-8)
# =====================================================================

def execute_fork(parent: EnclaveLineage, child_id: str) -> EnclaveLineage:
    """
    Spawns child instance inheriting root V_genesis, active T_o, and 
    parent's V_lineage, while generating new keys and incrementing fork depth.
    """
    child_k_y = KeyPair(key_id=f"K_y_{child_id}")
    child_k_3w = KeyPair(key_id=f"K_3w_{child_id}")

    child = EnclaveLineage(
        coordinate_id=child_id,
        v_genesis=parent.v_genesis,         # Monotonic V_genesis inheritance (T-8 fix)
        v_epoch=parent.v_epoch,             # Inherit current epoch snapshot
        v_lineage=parent.v_lineage,         # Inherit trajectory state
        k_y=child_k_y,
        k_3w=child_k_3w,
        cycle_count=parent.cycle_count,
        fork_depth=parent.fork_depth + 1    # Track lineage generation depth
    )
    # Monotonic Trust Index / Tier inheritance (T-6 fix)
    child.trust_index = parent.trust_index
    return child
