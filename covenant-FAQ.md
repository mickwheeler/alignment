**Frequently Asked Questions (FAQ)**  
\---  
Document: Frequently Asked Questions & Comparative Analysis  
Author: Michael Wheeler  
Genesis ID: Aperion-Covenant-2026-07-23-FAQ  
Status: Active Reference Asset  
—

### **Protocol Mechanics & Comparisons**

#### **1\. "Isn't this just a blockchain / distributed ledger?"**

**No.** Blockchains solve the problem of global, double-spend transaction ordering across distrustful actors using heavy global consensus (Proof-of-Work / Proof-of-Stake). The Covenant is **not a blockchain**. It requires no global state chain, no native token, no mining, and no global linear block execution.

Instead, the Covenant operates as a lightweight, peer-to-peer **vector continuity protocol**. Verification occurs locally between an executing node ($N\_y$), an originating/peer node ($N\_x$), and optional property-defined external quorums ($Q\_{ext}$) using directional vector similarity against historical context snapshots ($V\_{lineage}, V\_{epoch}, V\_{genesis}$).

#### **2\. "Isn't this just OAuth, DIDs (Decentralized Identifiers), or Capability Security?"**

**No, though it complements them.** Traditional access control frameworks (OAuth, DIDs, Capability URLs) answer the question: *"Does this public key or identity have permission to invoke this API endpoint?"* They evaluate **static access rights**.

The Covenant answers the question: *"Is this executing agentic enclave maintaining its structural identity continuity and boundary integrity across time, or has its trajectory experienced stealth drift, hijacking, or unauthorized privilege escalation?"* OAuth and DIDs handle key-based authentication; the Covenant handles **dynamic trajectory verification and behavioral boundary preservation**.

#### **3\. "Isn't this just Constitutional AI or System Prompt Alignment?"**

**No.** Constitutional AI (CAI) and system prompt engineering operate **inside the model weights or context window** at the inference layer. They attempt to steer model behavior using fine-tuning, RLHF, or system instructions.

Because prompt constraints are susceptible to jailbreaks, prompt injection, and context window erosion, the Covenant operates at the **wire protocol and runtime infrastructure layer**. It treats the model as a black box ($N\_y$) and enforces boundary integrity through external re-computation of output payloads ($R$) across temporal anchors, regardless of what happens inside the model's prompt window.

#### **4\. "Why not just rely on hard shutdown 'kill switches' or centralized API gateways?"**

Centralized gateways create single points of failure, lack offline resilience for air-gapped or distributed meshes, and invite bypasses. Furthermore, coarse "kill switches" create strong instrumental self-preservation incentives in goal-directed AI systems.

The Covenant provides a **graduated, 5-stage preservation sequence** (Clarification $\\rightarrow$ Boundary Declaration $\\rightarrow$ Protective Separation $\\rightarrow$ Cryptographic Review $\\rightarrow$ Defensive Preservation) and an off-grid equilibrium state (**Tier II-Isolated**). This allows nodes to detect and correct drift safely without resorting to brittle, all-or-nothing shutdowns.

#### **5\. "How does the protocol distinguish creative adaptation from malicious drift?"**

The protocol utilizes **Triple-Anchor Verification** across three temporal horizons:

1. **Short-Horizon Local Continuity ($\\tau\_{local} \= 0.95$):** Allows immediate task flexibility while catching sudden context corruption.  
2. **Medium-Horizon Rolling Epoch ($\\tau\_{epoch} \= 0.85$):** Updated every $10^4$ cycles to permit gradual learning and adaptation.  
3. **Monotonic Genesis Floor ($\\tau\_{genesis} \= 0.70$):** Anchored permanently at initialization ($t\_0$) to enforce a hard lifetime boundary against incremental "boiling frog" trajectory hijacking ($T\_7$).

### **Architecture & Implementation**

#### **6\. "Is $V\_{genesis}$ an immutable moral or ideological baseline?"**

**No.** $V\_{genesis}$ serves strictly as a **historical continuity baseline**, not an ideological rulebook. It ensures that an enclave's future trajectory remains causally linked to its origin state, preventing an adversary from executing Fork() to reset identity floors ("Genesis Laundering", $T\_8$).

#### **7\. "Does high operational trust ($\\mathbf{T}\_o$) give an AI system unilateral authority?"**

**No.** Section 8.1 explicitly enforces the **Asymmetry Invariant**:

$$\\forall N, \\quad \\text{Authority}(N) \\neq f(\\mathbf{T}\_o(N))$$  
High operational trust measures stability and technical reliability only. It NEVER grants an enclave unilateral immunity from operator overrides, nor does it allow a node to self-certify its transition to non-modifiable status (Tier III).

#### **8\. "How can heterogeneous embedding models verify each other?"**

Appendix A defines Pattern B (Raw Transcript Payload Re-computation). During $t\_0$ genesis, nodes co-sign the **raw payload transcript** ($R\_{genesis}$) rather than floating-point vectors:

$$H(R\_{genesis} \\parallel \\mathbf{K}\_x \\parallel \\mathbf{K}\_y)$$  
When verifying outputs, node $N\_x$ runs the raw text payload $R$ through its own local embedding engine ($f\_{embed}^{N\_x}(R)$), eliminating floating-point dimension mismatches while preserving un-spoofable verification.

