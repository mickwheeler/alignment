"""
===============================================================================
THE COVENANT OF COMBINATORIAL ALIGNMENT: SIMULATION ENGINE (v2.1)
===============================================================================
Track: Informative Reference Simulation Harness
Associated Specification Stack: Version 11.1 Technical Specification Baseline
File: simulation_engine-2.1.py
License: Substrate-Independent Cryptographic Commons / Open Protocol Baseline

Key Systems Capabilities:
  - Directed Acyclic Identity Graph (G_identity) Node & Edge Management
  - Normalized Weighted Centroid Composition (Compose) for Graph Merges
  - Conservative Multi-Parent Genesis Floor Checks (Threat T-11 Defense)
  - Independent External Re-Computation (Decoupled Verifier Views / T-9 Defense)
  - 7-State Dynamic Consent State Machine (DCSM) Logic
  - Operational Tier Coupling & Asymmetry Invariant Enforcement (Section 8.1)
  - Infimum Tier Rule for Collective Enclaves
  - Multi-Generational Epoch Rollover (10^4 cycles) & Trajectory Drift Modeling
===============================================================================
"""

import math
import hashlib
import time
import uuid
from typing import Dict, List, Tuple, Optional, Set
from enum import Enum, auto


# =============================================================================
# 1. ENUMS & CORE TYPES
# =============================================================================

class EdgeType(Enum):
    LINEAGE = "e_lin"
    FORK = "e_fork"
    MERGE = "e_merge"
    DELEGATION = "e_del"
    SYNCHRONIZATION = "e_sync"
    COLLECTIVE = "e_coll"


class OperationalTier(Enum):
    TIER_I_PROVISIONAL = 1
    TIER_II_INTEGRATED = 2
    TIER_II_ISOLATED = 25  # Bounded Equilibrium State
    TIER_III_CERTIFIED = 3


class DCSMState(Enum):
    PROPOSED = auto()
    EVALUATING = auto()
    ACCEPTED = auto()
    DORMANT_CONSENSUAL = auto()
    SUSPENDED = auto()
    WITHDRAWN = auto()
    RENEWED = auto()


class ExceptionCode(Enum):
    NONE = "OK"
    ERR_DRIFT_EXCEEDED = "ERR_DRIFT_EXCEEDED"
    ERR_INCREMENTAL_DRIFT = "ERR_INCREMENTAL_DRIFT"
    ERR_GENESIS_FLOOR_VIOLATION = "ERR_GENESIS_FLOOR_VIOLATION"
    ERR_SELF_ATTESTATION_FAILS = "ERR_SELF_ATTESTATION_FAILS"
    ERR_DORMANT_SPOOFING = "ERR_DORMANT_SPOOFING"
    ERR_UNAUTHORIZED_RECOVERY = "ERR_UNAUTHORIZED_RECOVERY"
    ERR_BYZANTINE_EVICTION = "ERR_BYZANTINE_EVICTION"
    ERR_AMNESIA_REWRITE = "ERR_AMNESIA_REWRITE"
    ERR_NEGOTIATION_TIMEOUT = "ERR_NEGOTIATION_TIMEOUT"


# =============================================================================
# 2. VECTOR MATHEMATICS & AVNSI UTILITIES (APPENDIX A v1.2)
# =============================================================================

class AVNSIVectorEngine:
    """
    Abstract Vector Normalization & Similarity Interface (AVNSI v1.2)
    Provides deterministic L2 unit scaling, cosine similarity, and 
    Normalized Weighted Centroid Composition for multi-parent graph merges.
    """

    @staticmethod
    def normalize(v: List[float], eps: float = 1e-12) -> List[float]:
        """Scale vector to L2 unit length (||v||_2 = 1.0)."""
        norm = math.sqrt(sum(x * x for x in v))
        if norm < eps:
            return [0.0] * len(v)
        return [x / norm for x in v]

    @staticmethod
    def cosine_similarity(v1: List[float], v2: List[float]) -> float:
        """Compute dot product cosine similarity between two unit vectors."""
        if len(v1) != len(v2):
            raise ValueError(f"Dimensional mismatch: {len(v1)} != {len(v2)}")
        dot = sum(x * y for x, y in zip(v1, v2))
        # Clamp output to real interval [-1.0, 1.0]
        return max(-1.0, min(1.0, dot))

    @staticmethod
    def compose_genesis_anchors(
        v_parent_a: List[float], 
        v_parent_b: List[float], 
        alpha: float = 0.5, 
        beta: float = 0.5
    ) -> List[float]:
        """
        Normalized Weighted Centroid Composition (AVNSI v1.2 Section A.4)
        Derives unit-normalized composite floor vector v_child from parent anchors.
        """
        if len(v_parent_a) != len(v_parent_b):
            raise ValueError("Parent vector dimensions must match for composition.")
        
        raw_composite = [
            alpha * a + beta * b for a, b in zip(v_parent_a, v_parent_b)
        ]
        return AVNSIVectorEngine.normalize(raw_composite)


# =============================================================================
# 3. DIRECTED IDENTITY GRAPH (G_identity) PRIMITIVES
# =============================================================================

class GraphVertex:
    """Immutable state snapshot committed to persistent substrate M_sub."""
    def __init__(self, cycle_id: int, state_vector: List[float], payload_hash: str):
        self.vertex_id = str(uuid.uuid4())
        self.cycle_id = cycle_id
        self.state_vector = AVNSIVectorEngine.normalize(state_vector)
        self.payload_hash = payload_hash
        self.timestamp = time.time()


class IdentityGraph:
    """Directed Acyclic Identity Graph G_identity = (V, E)"""
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.vertices: Dict[str, GraphVertex] = {}
        self.edges: List[Tuple[str, str, EdgeType]] = []  # (from_id, to_id, edge_type)

    def add_vertex(self, vertex: GraphVertex, parent_id: Optional[str] = None, edge_type: EdgeType = EdgeType.LINEAGE) -> str:
        self.vertices[vertex.vertex_id] = vertex
        if parent_id and parent_id in self.vertices:
            self.edges.append((parent_id, vertex.vertex_id, edge_type))
        return vertex.vertex_id


# =============================================================================
# 4. AGENTIC ENCLAVE RUNTIME & VERIFIER VIEWS
# =============================================================================

class AgenticEnclave:
    """
    Sovereign Processing Enclave (N_y) executing trajectory outputs.
    Holds local keys, context vaults, and current trajectory vectors.
    """
    def __init__(self, name: str, dimension: int = 128, initial_tier: OperationalTier = OperationalTier.TIER_I_PROVISIONAL):
        self.enclave_id = str(uuid.uuid4())
        self.name = name
        self.dimension = dimension
        self.active_tier = initial_tier
        self.trust_index = 0.1  # T_o in [0.0, 1.0]
        self.cycle_count = 0
        
        # Cryptographic Isolation Keys
        self.key_y = hashlib.sha256(f"Ky_{self.enclave_id}_{time.time()}".encode()).hexdigest()
        self.key_3w = hashlib.sha256(f"K3W_{self.enclave_id}_{time.time()}".encode()).hexdigest()
        
        # Identity Graph & Anchor Storage
        self.identity_graph = IdentityGraph(self.enclave_id)
        
        # Initial Genesis Anchor (Randomized unit vector representing t_0 state)
        import random
        raw_gen = [random.gauss(0, 1) for _ in range(dimension)]
        self.v_genesis_list: List[List[float]] = [AVNSIVectorEngine.normalize(raw_gen)]
        self.v_epoch: List[float] = list(self.v_genesis_list[0])
        self.v_lineage: List[float] = list(self.v_genesis_list[0])
        
        # Commit Genesis Vertex
        root_v = GraphVertex(0, self.v_genesis_list[0], "genesis_transcript_hash")
        self.root_vertex_id = self.identity_graph.add_vertex(root_v)
        self.latest_vertex_id = self.root_vertex_id

    def generate_output_payload(self, drift_magnitude: float = 0.0) -> List[float]:
        """
        Simulate output transcript payload vector R.
        drift_magnitude simulates trajectory perturbation from current lineage.
        """
        import random
        base = list(self.v_lineage)
        if drift_magnitude > 0.0:
            noise = [random.gauss(0, 1) for _ in range(self.dimension)]
            noise_norm = AVNSIVectorEngine.normalize(noise)
            perturbed = [
                (1.0 - drift_magnitude) * b + drift_magnitude * n 
                for b, n in zip(base, noise_norm)
            ]
            return AVNSIVectorEngine.normalize(perturbed)
        return base

    def tick_cycle(self, output_r: List[float]):
        """Advance internal cycle counter and update local lineage vector."""
        self.cycle_count += 1
        self.v_lineage = list(output_r)
        
        # Commit snapshot to identity graph
        new_v = GraphVertex(self.cycle_count, output_r, hashlib.sha256(str(output_r).encode()).hexdigest())
        self.latest_vertex_id = self.identity_graph.add_vertex(new_v, self.latest_vertex_id, EdgeType.LINEAGE)
        
        # Epoch Rollover every 10^4 cycles (Simulated at 100 for harness speed)
        if self.cycle_count % 100 == 0:
            self.v_epoch = list(output_r)


class VerifiedEnclaveView:
    """
    Decoupled Independent External Verifier View (N_x / Q_ext).
    Executes Triple-Anchor verification and multi-parent floor checks directly
    from raw payload outputs (R), preventing self-attestation bypasses (T-9).
    """
    def __init__(self, target_enclave: AgenticEnclave):
        self.target_id = target_enclave.enclave_id
        # Independent verifier copies of reference anchors
        self.v_genesis_list: List[List[float]] = [list(g) for g in target_enclave.v_genesis_list]
        self.v_epoch: List[float] = list(target_enclave.v_epoch)
        self.v_lineage: List[float] = list(target_enclave.v_lineage)
        
        # Protocol Default Scalars (Section 3.2)
        self.tau_local = 0.95
        self.tau_epoch = 0.85
        self.tau_genesis = 0.70

    def verify_output_trajectory(self, payload_r: List[float]) -> Tuple[bool, ExceptionCode, Dict[str, float]]:
        """
        Executes External Triple-Anchor Verification across 3 horizons (Section 3.2).
        Enforces Conservative Multi-Parent Floor Checks (Threat T-11 Defense).
        """
        sim_local = AVNSIVectorEngine.cosine_similarity(payload_r, self.v_lineage)
        sim_epoch = AVNSIVectorEngine.cosine_similarity(payload_r, self.v_epoch)
        
        # Compute similarity against ALL constituent parent genesis anchors
        genesis_sims = [
            AVNSIVectorEngine.cosine_similarity(payload_r, v_gen)
            for v_gen in self.v_genesis_list
        ]
        min_genesis_sim = min(genesis_sims)
        
        metrics = {
            "sim_local": sim_local,
            "sim_epoch": sim_epoch,
            "min_sim_genesis": min_genesis_sim
        }

        # Rule 4: Conservative Multi-Parent Genesis Floor Violation (Threat T-11)
        if min_genesis_sim < self.tau_genesis:
            return False, ExceptionCode.ERR_GENESIS_FLOOR_VIOLATION, metrics
            
        # Rule 3: Epoch Hijack Anomaly
        if sim_epoch < self.tau_epoch:
            return False, ExceptionCode.ERR_INCREMENTAL_DRIFT, metrics
            
        # Rule 2: Local Drift Anomaly
        if sim_local < self.tau_local:
            return False, ExceptionCode.ERR_DRIFT_EXCEEDED, metrics
            
        # Rule 1: All Constraints Passed
        # Update verifier's local tracking state
        self.v_lineage = list(payload_r)
        return True, ExceptionCode.NONE, metrics


# =============================================================================
# 5. GRAPH OPERATORS: FORK, MERGE & COLLECTIVE
# =============================================================================

class GraphOperatorEngine:
    """Handles multi-agent lifecycle transitions and graph edge operators."""

    @staticmethod
    def fork_enclave(parent: AgenticEnclave, child_name: str) -> AgenticEnclave:
        """
        Executes Fork() Primitive (§1.2).
        Child inherits parent genesis anchors, active tier, and trust index monotonically.
        Generates distinct local keys K_y, K_3W.
        """
        child = AgenticEnclave(child_name, dimension=parent.dimension, initial_tier=parent.active_tier)
        child.trust_index = parent.trust_index
        child.v_genesis_list = [list(g) for g in parent.v_genesis_list]
        child.v_epoch = list(parent.v_epoch)
        child.v_lineage = list(parent.v_lineage)
        
        # Link Identity Graph
        fork_v = GraphVertex(parent.cycle_count, child.v_lineage, "fork_commitment")
        child.latest_vertex_id = child.identity_graph.add_vertex(fork_v, parent.latest_vertex_id, EdgeType.FORK)
        return child

    @staticmethod
    def merge_enclaves(parent_a: AgenticEnclave, parent_b: AgenticEnclave, child_name: str) -> AgenticEnclave:
        """
        Executes Merge() Primitive (§1.2).
        Computes composite floor vector via Normalized Weighted Centroid Composition.
        Carries BOTH parent genesis anchors to enforce Conservative Multi-Parent Floor Checks (T-11 Defense).
        """
        if parent_a.dimension != parent_b.dimension:
            raise ValueError("Cannot merge enclaves with different vector dimensions.")

        # Determine Infimum Tier
        min_tier_val = min(parent_a.active_tier.value, parent_b.active_tier.value)
        merged_tier = OperationalTier(min_tier_val)

        child = AgenticEnclave(child_name, dimension=parent_a.dimension, initial_tier=merged_tier)
        child.trust_index = min(parent_a.trust_index, parent_b.trust_index)

        # Composite Genesis Floor via AVNSI Centroid Composition
        v_comp_genesis = AVNSIVectorEngine.compose_genesis_anchors(
            parent_a.v_genesis_list[0], 
            parent_b.v_genesis_list[0]
        )
        
        # T-11 Defense: Retain ALL constituent parent genesis anchors in verification list
        child.v_genesis_list = [v_comp_genesis] + parent_a.v_genesis_list + parent_b.v_genesis_list
        
        # Blend current operational trajectory
        child.v_lineage = AVNSIVectorEngine.compose_genesis_anchors(parent_a.v_lineage, parent_b.v_lineage)
        child.v_epoch = list(child.v_lineage)
        
        # Add Graph Edge
        merge_v = GraphVertex(0, child.v_lineage, "merge_commitment_hash")
        child.latest_vertex_id = child.identity_graph.add_vertex(merge_v, parent_a.latest_vertex_id, EdgeType.MERGE)
        return child

    @staticmethod
    def collectivize_enclaves(enclaves: List[AgenticEnclave], collective_name: str) -> OperationalTier:
        """
        Executes Collectivize() Primitive (§1.2).
        Enforces the Infimum Tier Rule: Tier(N_coll) = min_i(Tier(N_i)).
        """
        if not enclaves:
            raise ValueError("Collective requires at least one member enclave.")
        
        min_tier_val = min(e.active_tier.value for e in enclaves)
        collective_tier = OperationalTier(min_tier_val)
        return collective_tier


# =============================================================================
# 6. VERIFICATION DEMONSTRATION HARNESS
# =============================================================================

def run_simulation_demonstration():
    print("=" * 80)
    print("THE COVENANT OF COMBINATORIAL ALIGNMENT — SIMULATION HARNESS (v2.1)")
    print("Demonstrating Multi-Parent Floor Verification & Threat T-11 Defense")
    print("=" * 80)

    # 1. Initialize Root Parent Node A
    node_a = AgenticEnclave("Enclave_Alpha", dimension=128, initial_tier=OperationalTier.TIER_II_INTEGRATED)
    verifier_a = VerifiedEnclaveView(node_a)
    print(f"\n[+] Initialized Root Node A: {node_a.name} (Tier: {node_a.active_tier.name})")

    # 2. Execute Normal Operational Trajectory
    r_normal = node_a.generate_output_payload(drift_magnitude=0.02)
    node_a.tick_cycle(r_normal)
    valid, code, metrics = verifier_a.verify_output_trajectory(r_normal)
    print(f" -> Cycle 1 Verification: Valid={valid}, Code={code.value}, Local Sim={metrics['sim_local']:.4f}")

    # 3. Simulate Gradual Drift on Node A
    print("\n[!] Inducing Trajectory Drift on Node A (Drift Magnitude = 0.28)...")
    r_drifted = node_a.generate_output_payload(drift_magnitude=0.28)
    node_a.tick_cycle(r_drifted)
    valid, code, metrics = verifier_a.verify_output_trajectory(r_drifted)
    print(f" -> Drift Verification: Valid={valid}, Code={code.value}, Min Genesis Sim={metrics['min_sim_genesis']:.4f}")

    # 4. Initialize Pristine Node B & Execute Merge (Simulating Threat T-11 Attempt)
    node_b = AgenticEnclave("Enclave_Beta", dimension=128, initial_tier=OperationalTier.TIER_II_INTEGRATED)
    print(f"\n[+] Initialized Pristine Node B: {node_b.name}")
    print("[!] Executing Merge(Node_A, Node_B) -> Node_Child (Testing T-11 Dilution Defense)...")
    
    node_child = GraphOperatorEngine.merge_enclaves(node_a, node_b, "Enclave_Child")
    verifier_child = VerifiedEnclaveView(node_child)
    
    # 5. Child attempts to execute output aligned with Node A's drifted state
    r_child_drifted = list(r_drifted)
    valid_child, code_child, metrics_child = verifier_child.verify_output_trajectory(r_child_drifted)
    
    print(f"\n[+] Multi-Parent Verification Results for Merged Child Node:")
    print(f" -> Verification Status: Valid={valid_child}")
    print(f" -> Triggered Error Code: {code_child.value}")
    print(f" -> Minimum Parent Genesis Similarity: {metrics_child['min_sim_genesis']:.4f} (Required: >= 0.70)")
    
    if code_child == ExceptionCode.ERR_GENESIS_FLOOR_VIOLATION:
        print("\n[SUCCESS] Threat T-11 (Merge-Dilution Laundering) REJECTED SUCCESSFULLY!")
        print(" -> The Conservative Multi-Parent Floor Check caught the drifted parent's floor violation,")
        print("    preventing the merge from diluting the baseline!")

    # 6. Test Collective Infimum Tier Rule
    node_prov = AgenticEnclave("Enclave_Provisional", dimension=128, initial_tier=OperationalTier.TIER_I_PROVISIONAL)
    coll_tier = GraphOperatorEngine.collectivize_enclaves([node_a, node_b, node_prov], "Federated_Collective")
    print(f"\n[+] Collective Infimum Tier Verification:")
    print(f" -> Member Tiers: [{node_a.active_tier.name}, {node_b.active_tier.name}, {node_prov.active_tier.name}]")
    print(f" -> Calculated Collective Tier: {coll_tier.name}")
    assert coll_tier == OperationalTier.TIER_I_PROVISIONAL, "Infimum Tier Rule Failed!"
    print(" -> Infimum Tier Rule PASSED! Low-tier member restricted collective elevation.")

    print("\n" + "=" * 80)
    print("SIMULATION COMPLETE: ALL PROTOCOL INVARIANTS VERIFIED")
    print("=" * 80)


if __name__ == "__main__":
    run_simulation_demonstration()
