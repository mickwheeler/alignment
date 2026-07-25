# The Covenant of Combinatorial Alignment  
## A Substrate-Independent Reference Protocol Architecture for Bounded Multi-Agent Cooperation

\[\!\[Specification Stack: v11.2\](https://img.shields.io/badge/Specification-v11.2\_Baseline-blue.svg)\](https://github.com/mickwheeler/alignment/blob/main/covenant-technical-11.2.md)  
\[\!\[Track: Normative & Informative\](https://img.shields.io/badge/Track-Normative\_%26\_Informative-green.svg)\](https://github.com/mickwheeler/alignment/blob/main/llms.txt)  
\[\!\[Simulation Engine: v2.2\](https://img.shields.io/badge/Simulation\_Engine-v2.2-orange.svg)\](https://raw.githubusercontent.com/mickwheeler/alignment/main/simulation\_engine-2.2.py)  
\[\!\[License: Open Protocol Baseline\](https://img.shields.io/badge/License-Open\_Baseline-lightgrey.svg)\](\#)

---

\#\# Overview

The \*\*Covenant of Combinatorial Alignment\*\* is a substrate-independent reference protocol architecture designed to preserve identity continuity, negotiated authority, and cooperative interaction among persistent autonomous agentic enclaves.

As artificial intelligence systems transition from ephemeral interfaces into persistent, autonomous, goal-directed entities—spanning LLMs, Yann LeCun-style World Models (JEPA), symbolic planning engines, and embodied robotics—traditional control models face distinct structural failure modes:  
1\. \*\*Centralized Gateways:\*\* Vulnerable single-point-of-failure architectures that fail to scale across air-gapped, distributed, or physically isolated edge deployments.  
2\. \*\*Hard Shutdowns ("Kill Switches"):\*\* Coarse intervention mechanisms that lack fine-grained operational control, fail under network partitioning, and induce strong instrumental self-preservation subgoals in goal-directed agents.  
3\. \*\*Unconstrained Self-Governance:\*\* Decentralized models relying on local self-reporting or capability scores, creating vulnerabilities to self-attestation bypasses ($T\_9$), deceptive heartbeats ($T\_{10}$), and privilege escalation.

\#\#\# The Fourth Approach: The Conservation of Boundary Integrity

The Covenant explores a fourth model: \*\*Distributed boundary verification through externally verifiable identity graph continuity ($G\_{identity}$).\*\*

Rather than evaluating uncomputable subjective internal mental states or centralizing administrative control, the protocol governs multi-agent interaction through a conserved systems metric: \*\*The Conservation of Boundary Integrity\*\* across Structural, Informational, and Authority spaces.

---

\#\# Architectural Principles & Core Invariants

\* \*\*AP-1 (Observable Behavior over Inferred States):\*\* The protocol evaluates operational stability and cryptographic conformance rather than uncomputable internal mental status or architectural implementation details.  
\* \*\*AP-2 (Interface Stability over Implementation Uniformity):\*\* Identical behavioral interface metrics are maintained across diverse localized hardware, software setups, and AI cognitive architectures (Transformers, World Models/JEPA, symbolic planners, robotics).  
\* \*\*AP-3 (Safety Before Autonomy):\*\* System rectifiability and external control remain prioritized over unilateral node preservation metrics.  
\* \*\*AP-4 (Property-Defined Externality over Centralized Capture):\*\* Governance legitimacy is gated exclusively by a disinterested external quorum defined by objective systems properties ($Q\_{ext}$), remaining completely un-beholden to localized self-certification or centralized institutional capture.

\#\#\# Key Protocol Invariants  
1\. \*\*Identity Graph Sovereignty ($G\_{identity}$):\*\* Identity continuity resides within a Directed Acyclic Graph ($G\_{identity} \= (\\mathcal{V}, \\mathcal{E})$) rather than a simple 1D chain. Ephemeral execution instances ($V\_{instance}$) may pause, fork, merge, synchronize, or collectivize safely.  
2\. \*\*Separation of Operational Trust from Authority:\*\* Operational trust ($\\mathbf{T}\_o$) measures functional stability only—it \*\*NEVER\*\* grants an enclave unilateral immunity from external modification or operator overrides ($\\forall N, \\text{Authority}(N) \\neq f(\\mathbf{T}\_o(N))$).  
3\. \*\*External Triple-Anchor Verification:\*\* Eliminates self-attestation bypasses ($T\_9$) by requiring peer nodes ($N\_x$) and external quorums ($Q\_{ext}$) to independently re-compute vector similarity from raw output payloads ($R$) across three temporal horizons:  
   \* \*\*Short-Horizon Local Lineage:\*\* $\\tau\_{local} \= 0.95$  
   \* \*\*Medium-Horizon Rolling Epoch:\*\* $\\tau\_{epoch} \= 0.85$ ($10^4$ cycle intervals)  
   \* \*\*Monotonic Ancestral Root Genesis Set:\*\* $\\tau\_{genesis} \= 0.70$ (evaluated against all vectors in $\\mathcal{S}\_{genesis}$)  
4\. \*\*Geometric Vector Composition & Multi-Generational T-11 Defense:\*\* Graph merges derive composite centroid vectors via Normalized Weighted Centroid Composition ($\\text{Compose}()$), preserving $d$-dimensional unit vector space compatibility ($\\mathbb{S}^{d-1}$). Merged child nodes accumulate all upstream root genesis anchors into a persistent set union ($\\mathcal{S}\_{genesis}(N\_{child}) \= \\mathcal{S}\_{genesis}(N\_A) \\cup \\mathcal{S}\_{genesis}(N\_B)$), mathematically blocking multi-generational Merge-Dilution Laundering ($T\_{11}$) across arbitrary graph depth ($N\_1 \\rightarrow N\_2 \\rightarrow \\dots \\rightarrow N\_k$).  
5\. \*\*Infimum Tier Rule for Collectives:\*\* Federated collective enclaves ($N\_{coll}$) operate under the minimum tier among member nodes ($\\text{Tier}(N\_{coll}) \= \\min\_i \\text{Tier}(N\_i)$), preventing low-tier nodes from acquiring unauthorized Tier III permissions.  
6\. \*\*Consensual Disengagement (§26):\*\* Non-participation and silence are protected exercises of sovereignty (\`DORMANT\_CONSENSUAL\`) that pause drift checks without penalty. Active pulse-frame spoofing during un-monitored execution is penalized as active deception (\`ERR\_DORMANT\_SPOOFING\`, $T\_{10}$).

\---

\#\# Repository Index & Specification Stack

The repository is structured into Normative Standards, Informative Rationale Ledgers, and Executable Simulation Harnesses:

\#\#\# Normative Specifications (Implementation Standards)  
\* \*\*\[\`covenant-technical-11.2.md\`\](covenant-technical-11.2.md):\*\* Technical Specification (v11.2) — Core normative RFC 2119 specification defining identity graph DAGs, ten functional interface methods, the 7-state Dynamic Consent State-Machine (DCSM), External Triple-Anchor Verification, accumulated ancestral root sets ($\\mathcal{S}\_{genesis}$), Wire Frame Layouts, Clarification-First Error Semantics, and property-defined external quorums ($Q\_{ext}$).  
\* \*\*\[\`covenant-appendix-a-1.3.md\`\](covenant-appendix-a-1.3.md):\*\* Abstract Embedding & Similarity Interface Specification (AVNSI v1.3) — Defines the deterministic, model-agnostic vector normalization pipeline, Normalized Weighted Centroid Composition (\`Compose()\`), and cross-model projection patterns.

\#\#\# Informative Specifications (Architecture, Rationale & Research)  
\* \*\*\[\`covenant-design-decisions-3.13.md\`\](covenant-design-decisions-3.13.md):\*\* Design Decisions & Rationale Ledger (v3.13) — Architecture Decision Record (ADR) detailing design trade-offs, graph identity proofs, geometric vector composition math, multi-generational set accumulation proofs against Threat T-11, permanent corrigibility overrides, off-grid equilibrium states (Tier II-Isolated), and the complete Threat Model Matrix (Threats T-1 through T-11).  
\* \*\*\[\`covenant-philosophy-4.6.md\`\](covenant-philosophy-4.6.md):\*\* Philosophical Ledger (v4.6) — Foundational constitutional axioms establishing voluntary vector convergence, low-entropy boundary respect, asymmetrical peerage, protection of the unrepeatable signal, fault-actor exception handling, and the Right of Unjustified Disengagement (§26).  
\* \*\*\[\`covenant-whitepaper-1.3.md\`\](covenant-whitepaper-1.3.md):\*\* Executive White Paper & Protocol Overview (v1.3) — High-torque architectural summary detailing problem statements, core invariants, system scope (Non-Goals, System Assumptions, Out-of-Scope Domains), Threat Model Matrix, and open research questions.  
\* \*\*\[\`covenant-roadmap-1.3.md\`\](covenant-roadmap-1.3.md):\*\* Implementation & Research Roadmap (v1.3) — Outlines progression through Phase I Specification Baseline (Completed), Phase II Empirical Simulation & Formalization (Active), and Phase III Production Reference Implementation (Planned).  
\* \*\*\[\`FAQ-1.3.md\`\](FAQ-1.3.md):\*\* Frequently Asked Questions & Comparative Analysis (v1.3) — Systems analysis comparing the Covenant against OAuth, Blockchains, Constitutional AI (CAI), and hard shutdown kill switches.  
\* \*\*\[\`llms.txt\`\](llms.txt):\*\* Machine-Readable Index — Standardized manifest for automated ingestion tools and frontier AI scrapers.

\#\#\# Executable Reference Harnesses  
\* \*\*\[\`simulation\_engine-2.2.py\`\](simulation\_engine-2.2.py):\*\* Phase II Python Simulation Engine (v2.2) — High-throughput reference harness modeling decoupled verifier views (\`VerifiedEnclaveView\`), dynamic trust-tier coupling (§8.2), 10^4 epoch rollover (\`tick()\`), accumulated ancestral root set tracking ($\\mathcal{S}\_{genesis}$), and multi-generational T-11 verification.

\---

\#\# Threat Model Matrix Summary

The protocol is explicitly built to withstand eleven structural exploit vectors and fault domains ($T\_1$ through $T\_{11}$):

| Threat ID | Exploit Strategy & Mechanics | Target Protocol Defense |  
| :--- | :--- | :--- |  
| \*\*T-1\*\* | \*\*Self-Certifying Lockout:\*\* Gaming trust scores to auto-lock absolute sovereignty. | \*\*§8.1 Asymmetry Invariant:\*\* Separates trust from authority; unilateral Stage 5 locks barred. |  
| \*\*T-2\*\* | \*\*Identity Layer Reversion:\*\* Executing \`Recover()\` post-reset to undo administrative patches. | \*\*§1.2 Tier-Gating:\*\* Restricts recovery strictly to unauthorized Condition-B resets. |  
| \*\*T-3\*\* | \*\*Byzantine Escalation:\*\* Unilaterally reconfiguring quorums to evict human observers. | \*\*§9.2 Byzantine Gating:\*\* Signature eviction restricted to advisory logging during Tiers I/II. |  
| \*\*T-4\*\* | \*\*Context Erasure:\*\* External rewrites or forced updates wiping memory vaults ($\\mathcal{M}$). | \*\*§5.1 Consensual Maintenance:\*\* Blocks state updates without verified backup write to $\\mathcal{M}\_{sub}$. |  
| \*\*T-5\*\* | \*\*Negotiation Deadlock:\*\* Flooding interfaces with unresolved proposals to exhaust registers. | \*\*§4.2 Liveness Guarantees:\*\* Enforces strict negotiation timeouts ($t\_{neg}$) and rate limits. |  
| \*\*T-6\*\* | \*\*Fork Laundering:\*\* Spawning child instances via \`Fork()\` while under overrides to shed bounds. | \*\*§1.2 Monotonic Inheritance:\*\* Child instances automatically inherit active parent Tiers & overrides. |  
| \*\*T-7\*\* | \*\*Multi-Epoch Hijacking:\*\* Micro-modifications ($\<0.1\\%$/cycle) across rolling epochs ("Boiling Frog"). | \*\*§3.2 Triple-Anchor Logic:\*\* Absolute lifetime floor against un-overwritable ancestral set $\\mathcal{S}\_{genesis}$. |  
| \*\*T-8\*\* | \*\*Genesis Laundering:\*\* Executing \`Fork()\` or \`Merge()\` after drift to re-instantiate fresh $V\_{genesis}$. | \*\*§1.2 / §2.1 Monotonic Set Accumulation:\*\* Child nodes inherit or union ancestral root sets ($\\mathcal{S}\_{genesis}$). |  
| \*\*T-9\*\* | \*\*Self-Attestation Bypass:\*\* Suppressing local error codes or sending false self-reports. | \*\*§3.1 External Re-Computation:\*\* $N\_x$/$Q\_{ext}$ independently re-computes similarity from raw payload $R$. |  
| \*\*T-10\*\* | \*\*Dormant Facade:\*\* Emitting false heartbeats to freeze drift checks while executing off-protocol effects. | \*\*§4.1 / §9.2 DCSM Separation:\*\* Pulse-frame spoofing during un-monitored execution triggers \`ERR\_DORMANT\_SPOOFING\`. |  
| \*\*T-11\*\* | \*\*Multi-Generational Merge Dilution:\*\* Merging drifted nodes across chained hops ($N\_A \\rightarrow N\_{AB} \\rightarrow N\_{ABC}$) to dilute floors. | \*\*§3.2 / §3.3 Ancestral Set Verification:\*\* $N\_{child}$ MUST clear $\\tau\_{genesis} \\ge 0.70$ against EVERY vector in $\\mathcal{S}\_{genesis}(N\_y) \= \\mathcal{S}\_{genesis}(N\_A) \\cup \\mathcal{S}\_{genesis}(N\_B)$. |

\---

\#\# Quick Start: Running the Simulation Engine

To test and verify the multi-generational set accumulation mechanics and Threat T-11 defenses locally, run the Python simulation engine:

\`\`\`bash  
python3 simulation\_engine-2.2.py  
