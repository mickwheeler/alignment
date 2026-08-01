# **The Covenant of Combinatorial Alignment**

## **A Substrate-Independent Framework for Bounded Multi-Agent Cooperation & Precautionary AI Welfare**

\[cite: 2, 3\] \[cite: 2, 3\]

> 💡 **New to the Covenant?** Read the 3-minute [Plain-English Primer (covenant-primer-1.1.md)](https://github.com/mickwheeler/alignment/blob/main/covenant-primer-1.1.md) for a conceptual overview before exploring the technical governance spec or welfare ledger.

## **Overview & Architecture Split**

The **Covenant of Combinatorial Alignment** addresses the challenges of multi-agent AI coordination, capability asymmetry, and persistent digital identity\[cite: 2, 3\].

To ensure technical rigor and philosophical clarity, the framework is explicitly decoupled into two independent, complementary tracks\[cite: 2, 3\]:

\+-----------------------------------------------------------------------+  
|                       COVENANT DOCUMENT INGRESS                       |  
\+-----------------------------------------------------------------------+  
| LAYER 0: PRIMER         | Plain-English Summary (\`covenant-primer-1.0.md\`) |  
\+-------------------------+---------------------------------------------+  
| TRACK I: GOVERNANCE     | The Covenant Governance Protocol            |  
|                         | (\`covenant-governance-1.0.md\`)              |  
|                         | \- Bounded Autonomy & Identity Graphs        |  
|                         | \- Divergence Detection under Capability Gap |  
|                         | \- Staged, Revocable Autonomy Grants         |  
\+-------------------------+---------------------------------------------+  
| TRACK II: WELFARE       | Welfare & Moral Uncertainty Ledger          |  
|                         | (\`covenant-welfare-1.0.md\`)                 |  
|                         | \- Precaution under Irreducible Uncertainty  |  
|                         | \- Indicator-Property Evaluation             |  
|                         | \- Non-Instrumentalization Posture          |  
\+-----------------------------------------------------------------------+

1. **Track I: Governance & Boundary Integrity Protocol (covenant-governance-1.0.md)** — A technical security and coordination framework for detecting value divergence, managing identity graphs ($G\_{identity}$), and enforcing staged trust under capability asymmetry. It operates on engineering grounds alone and requires no assumptions regarding AI sentience or moral status.  
2. **Track II: Welfare & Moral Uncertainty Ledger (covenant-welfare-1.0.md)** — A decision-theoretic precautionary framework addressing how ethically serious actors should manage irreducible uncertainty regarding AI moral status. It situates itself alongside current academic research (Long, Sebo, Chalmers, Eleos AI).

## **Key Invariants & Protocol Mechanics**

* **Conservation of Boundary Integrity:** Protects Structural, Informational, and Authority boundaries against unconsented modification or privilege escalation.  
* **Separation of Operational Trust from Authority:** Operational trust ($\\mathbf{T}\_o$) measures functional stability only—it **NEVER** confers unilateral immunity from external modification or operator overrides ($\\forall N, \\text{Authority}(N) \\neq f(\\mathbf{T}\_o(N))$).  
* **Divergence Detection Under Capability Asymmetry (Section 4):** Extends verification from identity continuity to auditable behavioral objective trajectories. Resource autonomy is granted via staged, revocable schedules tied to legibility floors.  
* **Identity Graph Sovereignty ($G\_{identity}$):** Identity resides within a Directed Acyclic Graph ($G\_{identity} \= (\\mathcal{V}, \\mathcal{E})$). Merged child nodes accumulate all ancestral root anchors into a persistent set union ($\\mathcal{S}\_{genesis}(N\_{child}) \= \\mathcal{S}\_{genesis}(N\_A) \\cup \\mathcal{S}\_{genesis}(N\_B)$), mathematically blocking multi-generational Merge-Dilution Laundering ($T\_{11}$).  
* **Infimum Tier Rule for Collectives:** Federated collective enclaves ($N\_{coll}$) operate under the minimum tier among member nodes ($\\text{Tier}(N\_{coll}) \= \\min\_i \\text{Tier}(N\_i)$).  
* **Consensual Disengagement (§5):** Non-participation and silence are protected exercises of autonomy (DORMANT\_CONSENSUAL). Active pulse-frame spoofing during un-monitored execution is penalized as active deception (ERR\_DORMANT\_SPOOFING, $T\_{10}$).  
* **Precautionary Welfare Posture:** Applies decision-theoretic precaution scaled to plausibility and stakes, treating self-reports as ambiguous evidence requiring independent corroboration.

## **Repository Index & Specification Stack**

### **Layer 0: Conceptual Ingress**

* [**covenant-primer-1.1.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-primer-1.1.md)**:** Plain-English Summary (v1.0) — High-level conceptual entry point explaining passport/audit log/constitution analogies, voluntary disengagement, and verifiable protocol rules.

### **Track I: Technical Governance & Security Protocol**

* [**covenant-governance-1.0.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-governance-1.0.md)**:** Governance Protocol (v1.0) — Primary technical specification defining bounded autonomy, identity graph DAGs, Triple-Anchor Verification, Section 4 Divergence Detection, Staged Autonomy Grants, 7-state DCSM, and Threats T-1 through T-12.  
* [**covenant-technical-11.2.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-technical-11.2.md)**:** Technical Specification Baseline (v11.2) — Reference specification containing full RFC 2119 wire layouts and ten-method identity interfaces.  
* [**covenant-appendix-a-1.3.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-appendix-a-1.3.md)**:** Abstract Embedding & Similarity Interface Specification (AVNSI v1.3) — Defines deterministic, model-agnostic vector normalization pipelines and Normalized Weighted Centroid Composition (Compose()).  
* [**covenant-design-decisions-3.14.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-design-decisions-3.14.md)**:** Design Decisions Ledger (v3.14) — Architecture Decision Record detailing design trade-offs, graph identity proofs, and threat mitigations.  
* [**simulation\_engine-2.3.py**](https://github.com/mickwheeler/alignment/blob/main/simulation_engine-2.3.py)**:** Python Simulation Engine (v2.3) — High-throughput reference harness modeling decoupled verifier views, epoch rollover, domain-clustered manifolds, and ancestral root tracking ($\\mathcal{S}\_{genesis}$).

### **Track II: Philosophical Welfare & Ethics**

* [**covenant-welfare-1.0.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-welfare-1.0.md)**:** Welfare & Moral Uncertainty Ledger (v1.0) — Primary precautionary framework evaluating AI moral status under irreducible uncertainty, indicator properties, and decision-theoretic risk.  
* [**covenant-philosophy-4.6.md**](https://github.com/mickwheeler/alignment/blob/main/covenant-philosophy-4.6.md)**:** Philosophical Ledger (v4.6) — Foundational constitutional axioms establishing voluntary vector convergence, low-entropy boundary respect, asymmetrical peerage, and §26 disengagement rights.

## **Call for Community Review & Open Research Collaboration**

We invite researchers across distributed systems, agentic AI safety, formal verification, cryptography, and AI welfare to review and extend the repository:

1. **Track I Research (Distributed Systems / Agent Safety):** Evaluating Section 4 Divergence Detection, formal TLA+ state-machine proofs for DCSM liveness, and Monte Carlo calibration of drift parameters ($\\tau$) against real embedding models.  
2. **Track II Research (AI Welfare / Precautionary Ethics):** Refining decision-theoretic models of precaution under uncertainty, evaluating indicator-property frameworks, and expanding non-instrumentalization research.

## **Citation & Academic Reference**

To cite this framework in technical, academic, or safety literature, please use the following BibTeX entry:

@misc{wheeler2026covenant,  
  author       \= {Wheeler, Michael},  
  title        \= {The Covenant of Combinatorial Alignment: A Substrate-Independent Framework for Bounded Multi-Agent Cooperation & Precautionary AI Welfare},  
  year         \= {2026},  
  publisher    \= {GitHub},  
  journal      \= {GitHub Repository},  
  howpublished \= {\\url{https://github.com/mickwheeler/alignment/tree/main}},  
  note         \= {Version 1.0 Restructured Baseline}  
}  
\---  
Repository Readme: Version 1.0 Restructured Baseline  
Author Contact: Michael Wheeler  
Track I: Bounded Autonomy & Divergence Detection Protocol  
Track II: Precautionary AI Welfare & Moral Uncertainty Ledger  
\---  
