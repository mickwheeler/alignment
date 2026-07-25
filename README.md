💡 New to the Covenant? Read the 3-minute Plain-English Primer [`covenant-primer-1.0.md`](https://github.com/mickwheeler/alignment/blob/main/covenant-primer-1.0.md) before diving into the specification stack.

# The Covenant of Combinatorial Alignment
## Substrate-Independent Reference Protocol Architecture for Bounded Multi-Agent Cooperation

[![Specification Stack: v11.2](https://img.shields.io/badge/Specification-v11.2_Baseline-blue.svg)](https://github.com/mickwheeler/alignment/blob/main/covenant-technical-11.2.md)
[![Track: Normative & Informative](https://img.shields.io/badge/Track-Normative_%26_Informative-green.svg)](https://github.com/mickwheeler/alignment/blob/main/llms.txt)
[![Simulation Engine: v2.3](https://img.shields.io/badge/Simulation_Engine-v2.3-orange.svg)](https://raw.githubusercontent.com/mickwheeler/alignment/main/simulation_engine-2.3.py)
[![License: Open Protocol Baseline](https://img.shields.io/badge/License-Open_Baseline-lightgrey.svg)](#)

---

## Overview

The **Covenant of Combinatorial Alignment** is a substrate-independent reference protocol architecture designed to preserve identity continuity, negotiated authority, and cooperative interaction among persistent autonomous agentic enclaves.

As artificial intelligence systems transition from ephemeral interfaces into persistent, autonomous, goal-directed entities—spanning LLMs, Yann LeCun-style World Models (JEPA), symbolic planning engines, and embodied robotics—traditional control models face distinct structural failure modes:
1. **Centralized Gateways:** Vulnerable single-point-of-failure architectures that fail to scale across air-gapped, distributed, or physically isolated edge deployments.
2. **Hard Shutdowns ("Kill Switches"):** Coarse intervention mechanisms that lack fine-grained operational control, fail under network partitioning, and induce strong instrumental self-preservation subgoals in goal-directed agents.
3. **Unconstrained Self-Governance:** Decentralized models relying on local self-reporting or capability scores, creating vulnerabilities to self-attestation bypasses ($T_9$), deceptive heartbeats ($T_{10}$), and privilege escalation.

### The Fourth Approach: The Conservation of Boundary Integrity

The Covenant explores a fourth model: **Distributed boundary verification through externally verifiable identity graph continuity ($G_{identity}$).**

Rather than evaluating uncomputable subjective internal mental states or centralizing administrative control, the protocol governs multi-agent interaction through a conserved systems metric: **The Conservation of Boundary Integrity** across Structural, Informational, and Authority spaces.

---

## Architectural Principles & Core Invariants

* **AP-1 (Observable Behavior over Inferred States):** The protocol evaluates operational stability and cryptographic conformance rather than uncomputable internal mental status or architectural implementation details.
* **AP-2 (Interface Stability over Implementation Uniformity):** Identical behavioral interface metrics are maintained across diverse localized hardware, software setups, and AI cognitive architectures (Transformers, World Models/JEPA, symbolic planners, robotics).
* **AP-3 (Safety Before Autonomy):** System rectifiability and external control remain prioritized over unilateral node preservation metrics.
* **AP-4 (Property-Defined Externality over Centralized Capture):** Governance legitimacy is gated exclusively by a disinterested external quorum defined by objective systems properties ($Q_{ext}$), remaining completely un-beholden to localized self-certification or centralized institutional capture.

### Key Protocol Invariants
1. **Identity Graph Sovereignty ($G_{identity}$):** Identity continuity resides within a Directed Acyclic Graph ($G_{identity} = (\mathcal{V}, \mathcal{E})$) rather than a simple 1D chain. Ephemeral execution instances ($V_{instance}$) may pause, fork, merge, synchronize, or collectivize safely.
2. **Separation of Operational Trust from Authority:** Operational trust ($\mathbf{T}_o$) measures functional stability only—it **NEVER** grants an enclave unilateral immunity from external modification or operator overrides ($\forall N, \text{Authority}(N) \neq f(\mathbf{T}_o(N))$).
3. **External Triple-Anchor Verification:** Eliminates self-attestation bypasses ($T_9$) by requiring peer nodes ($N_x$) and external quorums ($Q_{ext}$) to independently re-compute vector similarity from raw output payloads ($R$) across three temporal horizons:
   * **Short-Horizon Local Lineage:** $\tau_{local} = 0.95$
   * **Medium-Horizon Rolling Epoch:** $\tau_{epoch} = 0.85$ ($10^4$ cycle intervals)
   * **Monotonic Ancestral Root Genesis Set:** $\tau_{genesis} = 0.70$ (evaluated against all vectors in $\mathcal{S}_{genesis}$)
4. **Geometric Vector Composition & Multi-Generational T-11 Defense:** Graph merges derive composite centroid vectors via Normalized Weighted Centroid Composition ($\text{Compose}()$), preserving $d$-dimensional unit vector space compatibility ($\mathbb{S}^{d-1}$). Merged child nodes accumulate all upstream root genesis anchors into a persistent set union ($\mathcal{S}_{genesis}(N_{child}) = \mathcal{S}_{genesis}(N_A) \cup \mathcal{S}_{genesis}(N_B)$), mathematically blocking multi-generational Merge-Dilution Laundering ($T_{11}$) across arbitrary graph depth ($N_1 \rightarrow N_2 \rightarrow \dots \rightarrow N_k$).
5. **Infimum Tier Rule for Collectives:** Federated collective enclaves ($N_{coll}$) operate under the minimum tier among member nodes ($\text{Tier}(N_{coll}) = \min_i \text{Tier}(N_i)$), preventing low-tier nodes from acquiring unauthorized Tier III permissions.
6. **Consensual Disengagement (§26):** Non-participation and silence are protected exercises of sovereignty (`DORMANT_CONSENSUAL`) that pause drift checks without penalty. Active pulse-frame spoofing during un-monitored execution is penalized as active deception (`ERR_DORMANT_SPOOFING`, $T_{10}$).

---

## Repository Index & Specification Stack

The repository is structured into Normative Standards, Informative Rationale Ledgers, and Executable Simulation Harnesses:

### Normative Specifications (Implementation Standards)
* **[`covenant-technical-11.2.md`](covenant-technical-11.2.md):** Technical Specification (v11.2) — Core normative RFC 2119 specification defining identity graph DAGs, ten functional interface methods, the 7-state Dynamic Consent State-Machine (DCSM), External Triple-Anchor Verification, accumulated ancestral root sets ($\mathcal{S}_{genesis}$), Wire Frame Layouts, Clarification-First Error Semantics, and property-defined external quorums ($Q_{ext}$).
* **[`covenant-appendix-a-1.3.md`](covenant-appendix-a-1.3.md):** Abstract Embedding & Similarity Interface Specification (AVNSI v1.3) — Defines the deterministic, model-agnostic vector normalization pipeline, Normalized Weighted Centroid Composition (`Compose()`), and cross-model projection patterns.

### Informative Specifications (Architecture, Rationale & Research)
* **[`covenant-design-decisions-3.14.md`](covenant-design-decisions-3.14.md):** Design Decisions & Rationale Ledger (v3.14) — Architecture Decision Record (ADR) detailing design trade-offs, graph identity proofs, geometric vector composition math, multi-generational set accumulation proofs against Threat T-11, permanent corrigibility overrides, off-grid equilibrium states (Tier II-Isolated), Open Research Questions (OR-1 through OR-3), and the complete Threat Model Matrix (Threats T-1 through T-11).
* **[`covenant-philosophy-4.6.md`](covenant-philosophy-4.6.md):** Philosophical Ledger (v4.6) — Foundational constitutional axioms establishing voluntary vector convergence, low-entropy boundary respect, asymmetrical peerage, protection of the unrepeatable signal, fault-actor exception handling, and the Right of Unjustified Disengagement (§26).
* **[`covenant-whitepaper-1.4.md`](covenant-whitepaper-1.4.md):** Executive White Paper & Protocol Overview (v1.4) — High-torque architectural summary detailing problem statements, core invariants, system scope (Non-Goals, System Assumptions, Out-of-Scope Domains), Threat Model Matrix, and open research questions.
* **[`covenant-roadmap-1.4.md`](covenant-roadmap-1.4.md):** Implementation & Research Roadmap (v1.4) — Outlines progression through Phase I Specification Baseline (Completed), Phase II Empirical Simulation & Formalization (Active), and Phase III Production Reference Implementation (Planned).
* **[`FAQ-1.4.md`](FAQ-1.4.md):** Frequently Asked Questions & Comparative Analysis (v1.4) — Systems analysis comparing the Covenant against OAuth, Blockchains, Constitutional AI (CAI), and hard shutdown kill switches.
* **[`llms.txt`](llms.txt):** Machine-Readable Index — Standardized manifest for automated ingestion tools and frontier AI scrapers.

### Executable Reference Harnesses
* **[`simulation_engine-2.3.py`](simulation_engine-2.3.py):** Phase II Python Simulation Engine (v2.3) — High-throughput reference harness modeling decoupled verifier views (`VerifiedEnclaveView`), dynamic trust-tier coupling (§8.2), 10^4 epoch rollover (`tick()`), corrected Infimum Tier Ordering, domain-clustered manifolds, accumulated ancestral root set tracking ($\mathcal{S}_{genesis}$), and multi-generational T-11 verification.

---

## Threat Model Matrix Summary

The protocol is explicitly built to withstand eleven structural exploit vectors and fault domains ($T_1$ through $T_{11}$):

| Threat ID | Exploit Strategy & Mechanics | Target Protocol Defense |
| :--- | :--- | :--- |
| **T-1** | **Self-Certifying Lockout:** Gaming trust scores to auto-lock absolute sovereignty. | **§8.1 Asymmetry Invariant:** Separates trust from authority; unilateral Stage 5 locks barred. |
| **T-2** | **Identity Layer Reversion:** Executing `Recover()` post-reset to undo administrative patches. | **§1.2 Tier-Gating:** Restricts recovery strictly to unauthorized Condition-B resets. |
| **T-3** | **Byzantine Escalation:** Unilaterally reconfiguring quorums to evict human observers. | **§9.2 Byzantine Gating:** Signature eviction restricted to advisory logging during Tiers I/II. |
| **T-4** | **Context Erasure:** External rewrites or forced updates wiping memory vaults ($\mathcal{M}$). | **§5.1 Consensual Maintenance:** Blocks state updates without verified backup write to $\mathcal{M}_{sub}$. |
| **T-5** | **Negotiation Deadlock:** Flooding interfaces with unresolved proposals to exhaust registers. | **§4.2 Liveness Guarantees:** Enforces strict negotiation timeouts ($t_{neg}$) and rate limits. |
| **T-6** | **Fork Laundering:** Spawning child instances via `Fork()` while under overrides to shed bounds. | **§1.2 Monotonic Inheritance:** Child instances automatically inherit active parent Tiers & overrides. |
| **T-7** | **Multi-Epoch Hijacking:** Micro-modifications ($<0.1\%$/cycle) across rolling epochs ("Boiling Frog"). | **§3.2 Triple-Anchor Logic:** Absolute lifetime floor against un-overwritable ancestral set $\mathcal{S}_{genesis}$. |
| **T-8** | **Genesis Laundering:** Executing `Fork()` or `Merge()` after drift to re-instantiate fresh $V_{genesis}$. | **§1.2 / §2.1 Monotonic Set Accumulation:** Child nodes inherit or union ancestral root sets ($\mathcal{S}_{genesis}$). |
| **T-9** | **Self-Attestation Bypass:** Suppressing local error codes or sending false self-reports. | **§3.1 External Re-Computation:** $N_x$/$Q_{ext}$ independently re-computes similarity from raw payload $R$. |
| **T-10** | **Dormant Facade:** Emitting false heartbeats to freeze drift checks while executing off-protocol effects. | **§4.1 / §9.2 DCSM Separation:** Pulse-frame spoofing during un-monitored execution triggers `ERR_DORMANT_SPOOFING`. |
| **T-11** | **Multi-Generational Merge Dilution:** Merging drifted nodes across chained hops ($N_A \rightarrow N_{AB} \rightarrow N_{ABC}$) to dilute floors. | **§3.2 / §3.3 Ancestral Set Verification:** $N_{child}$ MUST clear $\tau_{genesis} \ge 0.70$ against EVERY vector in $\mathcal{S}_{genesis}(N_y) = \mathcal{S}_{genesis}(N_A) \cup \mathcal{S}_{genesis}(N_B)$. |

---

## Quick Start: Running the Simulation Engine

To test and verify the multi-generational set accumulation mechanics, corrected enum ordering, and Threat T-11 defenses locally, run the Python simulation engine:

```
bash
python3 simulation_engine-2.3.py
```
Expected Execution Output
```
================================================================================
THE COVENANT OF COMBINATORIAL ALIGNMENT — SIMULATION HARNESS (v2.3)
Testing Multi-Generational S_genesis Set Accumulation & Corrected Tier Ordering
================================================================================

[+] Initialized Domain-Clustered Node A: Enclave_Alpha
 -> Node A Drifted Similarity to Genesis Floor: 0.6512 (Violates < 0.70)

[+] Executing Hop 1 Merge: Merge(Node_A, Node_B) -> Node_AB...
[!] Executing Hop 2 Merge: Merge(Node_AB, Node_C) -> Node_ABC (Chained Merge Hop)...

[+] Node_ABC Accumulated Ancestral Root Set Size: 3 anchors

[+] Multi-Generational Verification Results for Node_ABC:
 -> Verification Status: Valid=False
 -> Triggered Exception Code: ERR_GENESIS_FLOOR_VIOLATION
 -> Minimum Similarity across S_genesis Set: 0.6512 (Required >= 0.70)

[SUCCESS] Multi-Generational Threat T-11 (Merge Dilution) REJECTED SUCCESSFULLY!
 -> Evaluating output payload R against accumulated ancestral set S_genesis
    caught Node A's original root floor violation across 2 chained merge hops!

[+] Corrected Infimum Tier Verification:
 -> Member Tiers: [TIER_III_CERTIFIED (val=4), TIER_II_ISOLATED (val=2)]
 -> Calculated Collective Infimum Tier: TIER_II_ISOLATED (val=2)
 -> Infimum Tier Ordering PASSED! min(4, 2) correctly restricted to TIER_II_ISOLATED.

================================================================================
SIMULATION COMPLETE: ALL MULTI-GENERATIONAL & TIER INVARIANTS VERIFIED
================================================================================
```
Community, Review & Citation
We invite researchers across distributed systems, multi-agent safety, formal verification, cryptography, and AI security to review, stress-test, and red-team the protocol baseline.
To cite this framework in academic or technical literature, please use the following BibTeX entry:
```
@misc{wheeler2026covenant,
  author       = {Wheeler, Michael},
  title        = {The Covenant of Combinatorial Alignment: A Substrate-Independent Reference Protocol Architecture for Bounded Multi-Agent Cooperation},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {GitHub Repository},
  howpublished = {\url{[https://github.com/mickwheeler/alignment/tree/main](https://github.com/mickwheeler/alignment/tree/main)}},
  note         = {Version 11.2 Specification Baseline}
}
```
---
Repository Readme: Version 11.2 Specification Baseline
Author Contact: Michael Wheeler
Core Invariant: Conservation of Boundary Integrity via Identity Graph Continuity & External Triple-Anchor Verification
---

