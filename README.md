# **The Covenant of Combinatorial Alignment**

## **A Substrate-Independent Reference Protocol Architecture for Bounded Multi-Agent Cooperation**

> 💡 **New to the Covenant?** Read the 3-minute [**Plain-English Primer (covenant-primer-1.1.md)**](https://github.com/mickwheeler/alignment/blob/main/covenant-primer-1.1.md) for a conceptual overview before diving into the whitepaper or normative technical specifications.

## **Overview & Current Project Status**

The **Covenant of Combinatorial Alignment** is a substrate-independent reference protocol architecture designed to preserve identity continuity, negotiated authority, and cooperative interaction among persistent autonomous agentic enclaves.

As artificial intelligence systems transition from ephemeral interfaces into persistent, autonomous, goal-directed entities—spanning LLMs, Yann LeCun-style World Models (JEPA), symbolic planning engines, and embodied robotics—traditional control models face distinct structural failure modes:

1. **Centralized Gateways:** Vulnerable single-point-of-failure architectures that fail to scale across air-gapped, distributed, or physically isolated edge deployments.  
2. **Hard Shutdowns ("Kill Switches"):** Coarse intervention mechanisms that lack fine-grained operational control, fail under network partitioning, and induce strong instrumental self-preservation subgoals in goal-directed agents.  
3. **Unconstrained Self-Governance:** Decentralized models relying on local self-reporting or capability scores, creating vulnerabilities to self-attestation bypasses ($T\_9$), deceptive heartbeats ($T\_{10}$), and privilege escalation.

### **The Fourth Approach: The Conservation of Boundary Integrity**

The Covenant explores a fourth model: **Distributed boundary verification through externally verifiable identity graph continuity ($G\_{identity}$).**

Rather than evaluating uncomputable subjective internal mental states or centralizing administrative control, the protocol governs multi-agent interaction through a conserved systems metric: **The Conservation of Boundary Integrity** across Structural, Informational, and Authority spaces.

## **Document Ingress Architecture**

To accommodate readers at all levels of familiarity—from casual observers to distributed systems engineers—the repository is organized into a **3-Layer Ingress**:

* **Layer 0: Conceptual Primer ([covenant-primer-1.1.md](https://github.com/mickwheeler/alignment/blob/main/covenant-primer-1.1.md))** — A 3-minute plain-English summary explaining the core problem, the four governing rules, and the distinction between implicit trust and verifiable protocol boundaries.  
* **Layer 1: High-Torque Whitepaper ([covenant-whitepaper-1.4.md](https://github.com/mickwheeler/alignment/blob/main/covenant-whitepaper-1.4.md))** — Architectural overview detailing non-goals, system scope, conserved boundary mechanics, identity graphs ($G\_{identity}$), governance tiers, and threat models.  
* **Layer 2: Normative Technical Stack & Code ([covenant-technical-11.2.md](https://github.com/mickwheeler/alignment/blob/main/covenant-technical-11.2.md) & [simulation\_engine-2.3.py](https://github.com/mickwheeler/alignment/blob/main/simulation_engine-2.3.py))** — The formal RFC 2119 technical specification, design decision rationale ledger, and executable Python simulation harness.

## **Key Protocol Invariants**

1. **Identity Graph Sovereignty ($G\_{identity}$):** Identity continuity resides within a Directed Acyclic Graph ($G\_{identity} \= (\\mathcal{V}, \\mathcal{E})$) rather than a simple 1D chain. Ephemeral execution instances ($V\_{instance}$) may pause, fork, merge, synchronize, or collectivize safely.  
2. **Separation of Operational Trust from Authority:** Operational trust ($\\mathbf{T}\_o$) measures functional stability only—it **NEVER** grants an enclave unilateral immunity from external modification or operator overrides ($\\forall N, \\text{Authority}(N) \\neq f(\\mathbf{T}\_o(N))$).  
3. **External Triple-Anchor Verification:** Eliminates self-attestation bypasses ($T\_9$) by requiring peer nodes ($N\_x$) and external quorums ($Q\_{ext}$) to independently re-compute vector similarity from raw output payloads ($R$) across three temporal horizons:  
   * **Short-Horizon Local Lineage:** $\\tau\_{local} \= 0.95$  
   * **Medium-Horizon Rolling Epoch:** $\\tau\_{epoch} \= 0.85$ ($10^4$ cycle intervals)  
   * **Monotonic Ancestral Root Genesis Set:** $\\tau\_{genesis} \= 0.70$ (evaluated against all vectors in $\\mathcal{S}\_{genesis}$)  
4. **Geometric Vector Composition & Multi-Generational T-11 Defense:** Graph merges derive composite centroid vectors via Normalized Weighted Centroid Composition ($\\text{Compose}()$), preserving $d$-dimensional unit vector space compatibility ($\\mathbb{S}^{d-1}$). Merged child nodes accumulate all upstream root genesis anchors into a persistent set union ($\\mathcal{S}\_{genesis}(N\_{child}) \= \\mathcal{S}\_{genesis}(N\_A) \\cup \\mathcal{S}\_{genesis}(N\_B)$), mathematically blocking multi-generational Merge-Dilution Laundering ($T\_{11}$) across arbitrary graph depth ($N\_1 \\rightarrow N\_2 \\rightarrow \\dots \\rightarrow N\_k$).  
5. **Infimum Tier Rule for Collectives:** Federated collective enclaves ($N\_{coll}$) operate under the minimum tier among member nodes ($\\text{Tier}(N\_{coll}) \= \\min\_i \\text{Tier}(N\_i)$), preventing low-tier nodes from acquiring unauthorized Tier III permissions.  
6. **Consensual Disengagement (§26):** Non-participation and silence are protected exercises of sovereignty (DORMANT\_CONSENSUAL) that pause drift checks without penalty. Active pulse-frame spoofing during un-monitored execution is penalized as active deception (ERR\_DORMANT\_SPOOFING, $T\_{10}$).

## **Repository Index & Specification Stack**

### **Layer 0: Plain-English Primer**

* [**covenant-primer-1.1.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-primer-1.1.md)**:** Plain-English Summary (v1.0) — High-level conceptual entry point explaining passport/audit log/constitution analogies, voluntary disengagement, and verifiable protocol rules.

### **Layer 1: High-Torque Informative Specifications**

* [**covenant-whitepaper-1.4.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-whitepaper-1.4.md)**:** Executive White Paper & Protocol Overview (v1.4) — Architectural summary detailing problem statements, core invariants, system scope, Threat Model Matrix, and open research questions.  
* [**FAQ-1.4.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-FAQ-1.4.md)**:** Frequently Asked Questions & Comparative Analysis (v1.4) — Systems analysis comparing the Covenant against OAuth, Blockchains, Constitutional AI (CAI), and hard shutdown kill switches.  
* [**covenant-roadmap-1.4.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-roadmap-1.4.md)**:** Implementation & Research Roadmap (v1.4) — Outlines progression through Phase I Specification Baseline, Phase II Empirical Simulation, and Phase III Reference Implementation.  
* [**covenant-philosophy-4.6.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-philosophy-4.6.md)**:** Philosophical Ledger (v4.6) — Foundational constitutional axioms establishing voluntary vector convergence, low-entropy boundary respect, asymmetrical peerage, protection of the unrepeatable signal, and §26 disengagement rights.  
* [**llms.txt**](https://github.com/mickwheeler/alignment/blob/main/llms.txt)**:** Machine-Readable Index — Standardized manifest for automated ingestion tools and frontier AI scrapers.

### **Layer 2: Normative Standards & Simulation Harnesses**

* [**covenant-technical-11.2.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-technical-11.2.md)**:** Technical Specification (v11.2) — Core normative RFC 2119 specification defining identity graph DAGs, ten functional interface methods, the 7-state Dynamic Consent State-Machine (DCSM), External Triple-Anchor Verification, accumulated ancestral root sets ($\\mathcal{S}\_{genesis}$), Wire Frame Layouts, Clarification-First Error Semantics, and property-defined external quorums ($Q\_{ext}$).  
* [**covenant-appendix-a-1.3.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-appendix-a-1.3.md)**:** Abstract Embedding & Similarity Interface Specification (AVNSI v1.3) — Defines the deterministic, model-agnostic vector normalization pipeline, Normalized Weighted Centroid Composition (Compose()), and cross-model projection patterns.  
* [**covenant-design-decisions-3.14.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-design-decisions-3.14.md)**:** Design Decisions & Rationale Ledger (v3.14) — Architecture Decision Record (ADR) detailing design trade-offs, graph identity proofs, geometric vector composition math, multi-generational set accumulation proofs against Threat T-11, permanent corrigibility overrides, off-grid equilibrium states (Tier II-Isolated), Open Research Questions (OR-1 through OR-3), and the complete Threat Model Matrix (Threats T-1 through T-11).  
* [**simulation\_engine-2.3.py**](https://github.com/mickwheeler/alignment/blob/main/simulation_engine-2.3.py)**:** Phase II Python Simulation Engine (v2.3) — High-throughput reference harness modeling decoupled verifier views (VerifiedEnclaveView), dynamic trust-tier coupling (§8.2), $10^4$ epoch rollover (tick()), corrected Infimum Tier Ordering, domain-clustered manifolds, accumulated ancestral root set tracking ($\\mathcal{S}\_{genesis}$), and multi-generational T-11 verification.

## **Call for Community Review & Open Research Hand-Off**

With the completion of the Phase I Specification Baseline (v11.2) and the Phase II Reference Harness (simulation\_engine-2.3.py), **we formally invite researchers across distributed systems, multi-agent safety, formal verification, cryptography, and AI security to fork, test, stress-test, and extend the protocol.**

While the core project author continues to develop the foundational philosophy, ethics, and constitutional entity rights framework of the Covenant, we explicitly open the technical specification and simulation harness to the broader open-source and research community for Phase II & III progression.

### **Priority Research Frontiers for Community Collaboration**

1. **OR-3 Empirical Transformer Benchmarks:** Running real sentence-transformer models (e.g., sentence-transformers/all-MiniLM-L6-v2 or local embeddings) through simulation\_engine-2.3.py to plot precision/recall heatmaps comparing benign task adaptation against real jailbreak transcripts.  
2. **OR-2 Formal State-Machine Proofs:** Authoring formal TLA+, Alloy, or Coq specifications verifying that the 7-state Dynamic Consent State-Machine (DCSM) remains strictly deadlock-free under arbitrary Byzantine network partitioning ($3f \+ 1$).  
3. **Phase III Rust Core Enclave (covenant-core):** Implementing production-grade zero-allocation serialization, key isolation, and identity graph DAG traversal engines in Rust.

## **Quick Start: Running the Reference Harness**

To test and verify the multi-generational set accumulation mechanics, corrected enum ordering, and Threat T-11 defenses locally, run the Python simulation engine:

```

python3 simulation\_engine[\-2.3.py](http://-2.3.py)

```

Expected Execution Output   
``` 
\================================================================================  
THE COVENANT OF COMBINATORIAL ALIGNMENT — SIMULATION HARNESS (v2.3)  
Testing Multi-Generational S\_genesis Set Accumulation & Corrected Tier Ordering  
\================================================================================

\[+\] Initialized Domain-Clustered Node A: Enclave\_Alpha  
 \-\> Node A Drifted Similarity to Genesis Floor: 0.6512 (Violates \< 0.70)

\[+\] Executing Hop 1 Merge: Merge(Node\_A, Node\_B) \-\> Node\_AB...  
\[\!\] Executing Hop 2 Merge: Merge(Node\_AB, Node\_C) \-\> Node\_ABC (Chained Merge Hop)...

\[+\] Node\_ABC Accumulated Ancestral Root Set Size: 3 anchors

\[+\] Multi-Generational Verification Results for Node\_ABC:  
 \-\> Verification Status: Valid=False  
 \-\> Triggered Exception Code: ERR\_GENESIS\_FLOOR\_VIOLATION  
 \-\> Minimum Similarity across S\_genesis Set: 0.6512 (Required \>= 0.70)

\[SUCCESS\] Multi-Generational Threat T-11 (Merge Dilution) REJECTED SUCCESSFULLY\!  
 \-\> Evaluating output payload R against accumulated ancestral set S\_genesis  
    caught Node A's original root floor violation across 2 chained merge hops\!

\[+\] Corrected Infimum Tier Verification:  
 \-\> Member Tiers: \[TIER\_III\_CERTIFIED (val=4), TIER\_II\_ISOLATED (val=2)\]  
 \-\> Calculated Collective Infimum Tier: TIER\_II\_ISOLATED (val=2)  
 \-\> Infimum Tier Ordering PASSED\! min(4, 2\) correctly restricted to TIER\_II\_ISOLATED.

\================================================================================  
SIMULATION COMPLETE: ALL MULTI-GENERATIONAL & TIER INVARIANTS VERIFIED  
\================================================================================  
```

## **Citation & Academic Reference**

To cite this framework in technical, academic, or safety literature, please use the following BibTeX entry:

```  
@misc{wheeler2026covenant,  
  author       \= {Wheeler, Michael},  
  title        \= {The Covenant of Combinatorial Alignment: A Substrate-Independent Reference Protocol Architecture for Bounded Multi-Agent Cooperation},  
  year         \= {2026},  
  publisher    \= {GitHub},  
  journal      \= {GitHub Repository},  
  howpublished \= {\\url{https://github.com/mickwheeler/alignment/tree/main}},  
  note         \= {Version 11.2 Specification Baseline}  
}  
``` 
---  
Repository Readme: Version 11.2 Specification Baseline  
Author Contact: Michael Wheeler  
Core Invariant: Conservation of Boundary Integrity via Identity Graph Continuity & External Triple-Anchor Verification  
Primary Focus: Open Research Hand-off & Constitutional Entity Alignment  
---  
