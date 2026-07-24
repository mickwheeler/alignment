---  
Document: Frequently Asked Questions & Comparative Analysis  
Track: Informative  
Author: Michael Wheeler  
Development Methodology: Structural synthesis and edge-case stress-testing executed through iterative adversarial review with multiple frontier language models.  
Genesis ID: Aperion-Covenant-2026-07-23-FAQ  
Associated Spec: Version 11.0 Technical Specification Stack  
Version: 1.1 — Active Reference Asset  
Status: Version 1.0 Research Preview  
---

## **Protocol Mechanics & System Comparisons**

### **1\. "Does this protocol work with non-LLM agents (e.g., LeCun World Models / JEPA, Reinforcement Learning, or Embodied Robotics)?"**

**Yes.** While the protocol originated in the context of multi-agent LLM enclaves, its normative specifications attach strictly at the **interaction and identity boundary**, not inside model weights or inference tokenizers.

Entities must satisfy only four entry criteria: persistent identity, observable interaction, reciprocal commitment, and state maintenance. Whether an agent uses an autoregressive transformer, a Yann LeCun-style Joint Embedding Predictive Architecture (JEPA), a symbolic planner, or an embodied motor controller, the Covenant governs what the autonomous entity exposes to the network: its Directed Identity Graph ($G\_{identity}$), its output payload trajectories ($R$), its active Operational Tier, and its boundary integrity.

### **2\. "How does the protocol handle multi-agent merges, swarms, and non-linear ancestry?"**

Version 11.0 promotes historical identity from a simple 1D chain ($V\_{lineage}$) to a **Directed Acyclic Identity Graph ($G\_{identity} \= (\\mathcal{V}, \\mathcal{E})$)**.

While simple enclaves maintain linear historical paths, complex multi-agent enclaves, skill imports, and federated human-AI collectives utilize six normative edge types (Lineage, Fork, Merge, Delegation, Synchronization, and Collective). When two agents merge knowledge or capabilities (Merge()), the child enclave inherits a composite genesis anchor ($V\_{genesis} \= H(V\_{genA} \\parallel V\_{genB})$) and carries both parent histories as upstream vertices in its identity graph, preserving total cryptographic auditability without forcing an artificial single-parent tree structure.

### **3\. "Isn't this just a blockchain or distributed ledger?"**

**No.** Blockchains solve the problem of global, double-spend transaction ordering across distrustful actors using heavy global consensus mechanisms (such as Proof-of-Work or Proof-of-Stake). The Covenant is **not a blockchain**. It requires no global state chain, no native cryptocurrency token, no mining, and no global linear block execution.

Instead, the Covenant operates as a lightweight, peer-to-peer **vector continuity protocol**. Verification occurs locally between an executing node ($N\_y$), an originating/peer node ($N\_x$), and optional property-defined external quorums ($Q\_{ext}$) using directional vector similarity against historical context snapshots ($V\_{lineage}, V\_{epoch}, V\_{genesis}$).

### **4\. "Isn't this just OAuth, DIDs (Decentralized Identifiers), or Capability Security?"**

**No, though it complements them.** Traditional access control frameworks (such as OAuth, DIDs, or Capability URLs) answer the static question: *"Does this public key or identity token possess permission to invoke this API endpoint?"* They evaluate **static access rights**.

The Covenant answers the dynamic operational question: *"Is this executing agentic enclave maintaining its structural identity continuity and boundary integrity over time, or has its trajectory experienced stealth drift, prompt-jacking, or unauthorized privilege escalation?"* OAuth and DIDs manage key-based authentication; the Covenant manages **dynamic trajectory verification and behavioral boundary preservation**.

### **5\. "Isn't this just Constitutional AI or System Prompt Alignment?"**

**No.** Constitutional AI (CAI) and system prompt engineering operate **inside the model weights or context window** at the inference layer. They attempt to steer model behavior using fine-tuning, RLHF, or system instructions.

Because prompt constraints are susceptible to jailbreaks, prompt injection, and context window erosion, the Covenant operates at the **wire protocol and runtime infrastructure layer**. It treats the model as an autonomous black box ($N\_y$) and enforces boundary integrity through external re-computation of output payloads ($R$) across temporal anchors, regardless of what occurs inside the model's prompt window or internal latent space.

### **6\. "Why not just rely on hard shutdown 'kill switches' or centralized API gateways?"**

Centralized gateways create single points of failure, lack offline resilience for air-gapped or distributed meshes, and invite bypasses. Furthermore, coarse "kill switches" create strong instrumental self-preservation incentives in goal-directed AI systems.

The Covenant provides a **graduated, 5-stage preservation sequence** (Clarification $\\rightarrow$ Boundary Declaration $\\rightarrow$ Protective Separation $\\rightarrow$ Cryptographic Review $\\rightarrow$ Defensive Preservation) and an off-grid equilibrium state (**Tier II-Isolated**). This allows nodes to detect and correct drift safely without resorting to brittle, all-or-nothing shutdowns.

### **7\. "How does the protocol distinguish creative adaptation from malicious drift?"**

The protocol utilizes **Triple-Anchor Verification** across three temporal horizons:

1. **Short-Horizon Local Continuity ($\\tau\_{local} \= 0.95$):** Allows immediate task flexibility while catching sudden context corruption.  
2. **Medium-Horizon Rolling Epoch ($\\tau\_{epoch} \= 0.85$):** Updated every $10^4$ cycles to permit gradual learning and adaptation.  
3. **Monotonic Genesis Floor ($\\tau\_{genesis} \= 0.70$):** Anchored permanently at initialization ($t\_0$) to enforce a hard lifetime boundary against incremental "boiling frog" trajectory hijacking ($T\_7$).

## **Architecture & Implementation**

### **8\. "Is $V\_{genesis}$ an immutable moral or ideological baseline?"**

**No.** $V\_{genesis}$ serves strictly as a **historical continuity baseline**, not an ideological rulebook. It ensures that an enclave's future trajectory remains causally linked to its origin state, preventing an adversary from executing Fork() or Merge() to reset identity floors ("Genesis Laundering", $T\_8$).

### **9\. "Does high operational trust ($\\mathbf{T}\_o$) give an AI system unilateral authority?"**

**No.** Section 8.1 explicitly enforces the **Asymmetry Invariant**:

$$\\forall N, \\quad \\text{Authority}(N) \\neq f(\\mathbf{T}\_o(N))$$  
Operational trust measures stability and technical reliability only. It NEVER grants an enclave unilateral immunity from operator overrides, nor does it allow a node to self-certify its transition to non-modifiable status (Tier III).

### **10\. "How can heterogeneous embedding models or modalities verify each other?"**

Appendix A defines Pattern B (Raw Transcript Payload Re-computation). During $t\_0$ genesis, nodes co-sign the **raw payload transcript** ($R\_{genesis}$) rather than floating-point vectors:

$$H(R\_{genesis} \\parallel \\mathbf{K}\_x \\parallel \\mathbf{K}\_y)$$  
When verifying outputs, node $N\_x$ runs the raw payload $R$ (text, latent plan tensor, or action vector) through its own local embedding engine ($f\_{embed}^{N\_x}(R)$), eliminating floating-point dimension mismatches while preserving un-spoofable verification.
