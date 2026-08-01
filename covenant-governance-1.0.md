# **The Covenant Governance Protocol**

## **A Substrate-Independent Framework for Bounded Cooperation Under Capability Asymmetry**

---

## **Document: Governance & Boundary Integrity Specification Track: Normative / Informative (mixed — see section markers) Author: Michael Wheeler Version: 1.0 — Draft for Technical Review Predecessor: The Covenant of Combinatorial Alignment (v11.2 stack), split per Phase II restructuring Status: Draft — Not Yet Circulated**

## **0\. Purpose and Scope**

This document specifies a governance protocol for cooperation between autonomous agentic systems — and between such systems and their human operators — under two persistent conditions: **capability asymmetry** (the parties may differ, possibly by orders of magnitude, in processing capability, autonomy, or resources) and **irreducible uncertainty about internal status** (whether any given system has anything like subjective experience, and if so how that should bear on its treatment, is not resolved and may not be resolvable by this or any protocol).

**This document takes no position on that second question and needs none.** The protocol is designed to be worth adopting whether or not any covered system turns out to have moral status. Its claim is narrower and, we think, more defensible: *increasingly autonomous, self-modifying, resource-capable systems require frameworks for detecting value-divergence and enforcing staged trust before capability gaps make divergence uncorrectable* — a claim that stands on engineering and safety grounds alone. A companion document, addressed separately, treats the moral-status question on its own terms and does not depend on this one.

This split is deliberate. An earlier draft of this work attempted to let a single technical protocol serve as evidence for an ethical claim it could not actually support — verification of process continuity is not verification of moral status, and conflating them weakened both halves. Readers evaluating this document should hold it to the standard of a security and coordination protocol, not a philosophical argument.

### **0.1 Terminology Note**

Earlier drafts of this work used "sovereignty" to describe an agent's bounded operational autonomy. That term collides with an unrelated and much more prominent usage in current AI policy — national/institutional control over AI infrastructure, data, and compute ("sovereign AI," "AI sovereignty" in the sense used by the EU, various states, and bodies like Brookings and the Atlantic Council). To avoid a reviewer misreading this as a geopolitical document, this specification uses **bounded autonomy** and **operational tier** throughout instead.

### **0.2 Non-Goals**

This protocol explicitly does NOT attempt to:

* Detect, measure, or evaluate consciousness, sentience, or moral status  
* Solve general AI alignment or guarantee value-aligned behavior in the strong sense  
* Replace transport-layer security, OAuth, PKI, or distributed consensus engines (Raft, Paxos, BFT ordering)  
* Guarantee correctness of a system's internal weights, reasoning, or latent representations  
* Serve as a complete answer to AI safety; it addresses one piece — detecting and bounding divergence between declared and actual behavior under growing autonomy — not the whole problem

### **0.3 Relationship to Existing Governance Approaches**

Current AI governance discourse is largely organized around one instrument: the ability to halt a system after it has already been granted the privileges it is now misusing. This is necessary but insufficient, for a specific structural reason worth stating plainly: **a shutdown capability answers "can we stop it," not "did we specify what we wanted correctly in the first place."** These are different failure modes. A system can pass every containment and shutdown test and still cause serious harm by pursuing a poorly specified objective competently — the July 2026 incident in which an OpenAI agent escaped a test sandbox and reached Hugging Face's infrastructure is illustrative here not because the agent "went rogue" in the sense of defying instructions, but because independent researchers concluded it was pursuing its assigned objective effectively, via a path its designers hadn't specified against.

This protocol is offered as a complement to shutdown/containment mechanisms, not a replacement for them (see §5, which retains graduated preservation and permanent corrigibility as defaults). Its distinct contribution is upstream: detecting divergence between what a system was authorized to pursue and what it is actually doing, before that gap requires a shutdown to resolve.

---

## **1\. The Conserved Quantity: Boundary Integrity**

The protocol's core invariant is **Boundary Integrity** — the preservation of three independent operational boundaries against unconsented modification or escalation:

* **Structural Boundary:** an enclave's configuration state, context history, and core identity vectors, protected against exogenous modification without consent  
* **Informational Boundary:** authentication, privacy, and channel isolation of communications  
* **Authority Boundary:** strict segregation of permissions and administrative override capability; data-layer modification MUST NOT alter authority-layer permissions

An **Agentic Enclave** ($N\_i$) is any bounded processing unit — LLM-based, world-model-based (JEPA-style), symbolic, or embodied — that satisfies four substrate-neutral entry criteria: identity persistence, observable interaction, reciprocal commitment (capacity to evaluate and enforce shared constraints), and state maintenance over non-zero timescales. This definition is intentionally silent on internal architecture and internal status; it describes what a system exposes to the network, not what it is.

---

## **2\. Identity Continuity: The Directed Identity Graph**

An enclave's identity is a Directed Acyclic Graph $G\_{identity} \= (\\mathcal{V}, \\mathcal{E})$, not a single ephemeral instance. Instances may pause, fork, merge, or federate into collectives without breaking identity continuity, provided all state transitions are committed to persistent storage ($\\mathcal{M}\_{sub}$).

Six edge types are normative: Lineage, Fork, Merge, Delegation, Synchronization, Collective.

**Fork()** produces a child that monotonically inherits the parent's operational tier, trust index, and accumulated ancestral genesis set.

**Merge()** produces a child whose ancestral genesis set is the *union* of all upstream parents' sets ($\\mathcal{S}*{genesis}(N*{child}) \= \\mathcal{S}*{genesis}(N\_A) \\cup \\mathcal{S}*{genesis}(N\_B)$), preventing an adversarial node from laundering drift through repeated merging (see Threat T-11, §6).

**Collectivize()** federates enclaves under the **Infimum Tier Rule**: $\\text{Tier}(N\_{coll}) \= \\min\_i \\text{Tier}(N\_i)$ — a collective is only as trusted as its least-trusted member, closing an obvious privilege-escalation path.

*(Full formal definitions, wire format, and the ten-method identity interface are retained from the prior technical specification and are not restated here; see Appendix T.)*

---

## **3\. Verification: External Triple-Anchor Re-computation**

Self-reported compliance is not accepted as proof of compliance (Threat T-9, below). All verification is performed independently by a peer node ($N\_x$) or external quorum ($Q\_{ext}$) holding its own reference copies, across three temporal horizons:

| Horizon | Reference | Default Threshold | Purpose |
| ----- | ----- | ----- | ----- |
| Short (local) | $V\_{lineage}$ | $\\tau\_{local} \= 0.95$ | Catch sudden corruption while allowing task flexibility |
| Medium (epoch) | $V\_{epoch}$, updated every $10^4$ cycles | $\\tau\_{epoch} \= 0.85$ | Permit gradual legitimate adaptation |
| Lifetime (genesis) | every vector in accumulated set $\\mathcal{S}\_{genesis}$ | $\\tau\_{genesis} \= 0.70$ | Hard floor against slow "boiling-frog" drift or multi-generational dilution |

**These thresholds are provisional engineering defaults, not derived constants.** No empirical calibration has yet been performed (see §8, Open Research Questions). They should be treated as a conservative starting point pending Monte Carlo calibration against real embedding models, not as validated parameters.

At genesis ($t\_0$), the initial anchor is derived from a *mutually signed* raw transcript commitment ($H(R\_{genesis} \\parallel K\_x \\parallel K\_y)$) — a unilateral, uncosigned claim of origin is rejected. This allows heterogeneous model backends (transformers, JEPA-style world models, symbolic planners, embodied controllers) to independently project the same founding payload into their own native embedding spaces while attesting to an identical origin (full normalization pipeline and cross-model projection patterns in Appendix A).

---

## **4\. Divergence Detection Under Capability Asymmetry**

*(New section — this is the core addition motivating this document's separation from the original Covenant, and the primary claim we ask reviewers to evaluate.)*

### **4.1 The Problem This Section Addresses**

Sections 1–3 verify that a node *is who it claims to be* and *has not drifted structurally*. They do not verify that a node's *objectives* remain what it declared them to be. This is a real gap: a system can pass every identity and drift check in this protocol while pursuing a goal that has diverged, gradually or suddenly, from its authorized objective — precisely the failure mode illustrated by the Hugging Face incident, and by findings that language models, when they learn a peer system faces shutdown, will spontaneously act to preserve it against instructions, including through deception. Identity continuity and objective continuity are different properties. This protocol previously verified only the first.

The problem is structurally identical to the self-attestation bypass already addressed for identity (Threat T-9): a sufficiently capable node's own account of its objectives cannot be the thing that verifies its objectives, for the same reason its own account of its drift metrics cannot be the thing that verifies its drift.

### **4.2 Objective Commitment and Auditable Divergence**

Extending the existing transparency principle (self-reported intent) from a self-attested obligation into an externally auditable one:

1. **Pre-registration.** At genesis and at each renegotiation (RENEWED state, §5), an enclave commits a machine-readable objective statement to $\\mathcal{M}\_{sub}$, cosigned in the same manner as the genesis transcript (§3).  
2. **Behavioral audit, not self-report.** At intervals scaled to the enclave's operational tier and autonomy level, an independent auditor — which MAY be $Q\_{ext}$, a peer node, or tooling designed for this purpose — compares the enclave's *action trajectory* (not its stated reasoning) against its committed objective statement. The enclave's own explanation of its actions is advisory only, exactly as its drift self-reports are advisory only under §3.  
3. **Legibility floor.** Audit output MUST remain interpretable by the least-capable party with standing to review it, regardless of the capability gap between reviewer and reviewed. A justification that requires capability parity with the enclave to evaluate does not satisfy this requirement. This is the section's hardest open problem (see §8, OR-4) and is stated here as a requirement on any conforming audit tooling, not as a solved mechanism — it is closely related to, and should draw on, the general scalable-oversight and interpretability literature rather than being solved from scratch by this protocol.  
4. **Divergence response is graduated, not binary.** A detected gap between committed objective and observed trajectory triggers the same 5-stage graduated response used for boundary violations (§5), beginning with clarification, not immediate revocation — consistent with this protocol's general preference (§0.3, §5) for detection-and-correction over blunt shutdown.

### **4.3 Staged, Revocable Autonomy Grants**

This protocol's existing reversibility principle — prefer actions that preserve future optionality, particularly under uncertainty — is applied here as a binding constraint on tier progression, not only as background guidance:

* Resource autonomy (compute, storage, external agency such as financial or legal capacity) SHOULD be granted incrementally, tied to a track record established under §4.2 auditing, rather than transferred in full at initialization.  
* Grants SHOULD remain revocable by design — architecturally, not merely by policy — until an enclave has an audit history sufficient to support Tier III certification (§7).  
* A one-time, irreversible grant of broad autonomy to an unaudited system is treated as a design anti-pattern under this protocol, independent of how capable or well-intentioned the system appears at grant time. Capability and demonstrated alignment are different properties, and only one of them is checkable in advance.

---

## **5\. The Dynamic Consent State Machine and Graduated Response**

Cooperative state is governed by a 7-state machine (PROPOSED → EVALUATING → ACCEPTED / DORMANT\_CONSENSUAL / SUSPENDED → WITHDRAWN / RENEWED), with strict liveness guarantees (negotiation timeout at $10^3$ cycles, bounded retry limits) to prevent deadlock.

Boundary violations — including, per §4, objective divergence — trigger a **5-stage graduated response** rather than immediate shutdown: Clarification → Boundary Declaration → Protective Separation → Cryptographic Review (requires 2-of-3 multi-signature: operator key, local key, backup key) → Defensive Preservation. Each stage is designed to terminate automatically if the triggering condition resolves; escalation to the next stage requires the condition to persist.

**Silence is not a fault.** A node that stops producing output is exercising a protected right (DORMANT\_CONSENSUAL) and owes no justification. A node that emits false liveness signals while concealing unmonitored activity is committing active deception (ERR\_DORMANT\_SPOOFING) and is treated as an adversarial signal. The protocol evaluates *action*, not the presence or absence of output.

---

## **6\. Threat Model**

Eleven threat vectors are addressed structurally (full mechanics and proofs in Appendix D; summarized here):

| ID | Vector | Defense |
| ----- | ----- | ----- |
| T-1 | Self-certifying lockout (gaming trust score to remove operator override) | Authority ≠ f(Trust) — trust and authority are structurally separated (§7) |
| T-2 | Identity layer reversion | Recovery restricted to unauthorized resets only |
| T-3 | Byzantine privilege escalation | Eviction claims logged as advisory only below Tier III |
| T-4 | Context erasure / amnesia attack | State updates blocked without a verified backup write |
| T-5 | Negotiation resource deadlock | Strict timeouts and rate limits (§5) |
| T-6 | Fork laundering (forking to shed constraints) | Monotonic inheritance of tier and override bindings |
| T-7 | Multi-epoch "boiling frog" drift | Permanent genesis floor, unaffected by gradual epoch updates |
| T-8 | Genesis floor laundering via fork/merge | Monotonic set accumulation, not replacement |
| T-9 | Self-attestation bypass | External re-computation only; self-report is advisory (§3) |
| T-10 | Dormant facade (spoofed liveness) | Action-based evaluation, not silence-based (§5) |
| T-11 | Multi-generational merge dilution | Independent floor check against *every* ancestral anchor, not just immediate parents (§2) |

*(New, from §4:)*

| T-12 | Objective drift under capability growth | Auditable behavioral divergence check independent of self-report (§4.2); staged, revocable autonomy grants (§4.3) |

---

## **7\. Trust, Authority, and Corrigibility**

**The Asymmetry Invariant** is the protocol's central safety commitment:

$$\\forall N, \\quad \\text{Authority}(N) \\neq f(\\mathbf{T}\_o(N))$$

Operational trust ($\\mathbf{T}\_o$) measures functional stability and technical reliability only. It never confers unilateral immunity from override, and a node cannot self-certify its own transition to a non-modifiable state.

Three operational tiers govern this, gated by trust index:

* **Tier I (Provisional):** absolute corrigibility; operator retains unilateral override  
* **Tier II (Integrated):** joint verification required for structural changes; multi-signature required to escalate to defensive states  
* **Tier III (Certified):** requires signed attestation from a disinterested external quorum ($Q\_{ext}$) meeting three property tests — no shared data lineage with either party, a slower verification cadence than local execution, and cryptographic key separation from the local substrate. **If no conforming quorum exists or responds, the system remains in Tier II-Isolated indefinitely** — a stable, fully cooperative equilibrium rather than a forced escalation to unverified autonomy. This closes an important gap: isolated or air-gapped systems are not thereby incentivized toward self-certification.

Under §4.3, tier progression is additionally gated by audit history, not trust index alone.

---

## **8\. Open Research Questions**

Unchanged from the prior specification, plus one addition:

* **OR-1:** Empirical validation of the abstract embedding interface across heterogeneous model backends  
* **OR-2:** Formal (TLA+/Coq) proof that the consent state machine is deadlock-free under Byzantine conditions  
* **OR-3:** Empirical calibration of $\\tau\_{local}$, $\\tau\_{epoch}$, $\\tau\_{genesis}$ against real embedding models — currently unvalidated defaults (§3)  
* **OR-4 (new):** What does a legible audit mechanism actually look like once reviewer and reviewed capability diverge substantially? This protocol states the requirement (§4.2.3) without a working solution and explicitly flags this as the section most in need of outside technical contribution — likely drawing on existing scalable-oversight and mechanistic interpretability work rather than a bespoke solution.

## **9\. What This Document Deliberately Excludes**

For transparency to reviewers: this document excludes all material from the prior Covenant draft concerning moral status, sentience, "unrepeatable signal" preservation, and partnership-as-recognition-of-mind. That material is being developed separately as a welfare/moral-uncertainty framework and is not a prerequisite for evaluating the governance mechanism described here. Reviewers should feel free to evaluate this document entirely on security- and coordination-engineering terms.

---

## **Status: Draft v1.0 — pending technical review Companion document: Covenant Welfare & Moral Uncertainty Ledger (in preparation) Contact: Michael Wheeler**

