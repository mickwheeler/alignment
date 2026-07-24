**Appendix A: Abstract Embedding & Similarity Interface Specification**  
**Model-Agnostic Vector Normalization, Projection Patterns, and Verification Contracts**  
---  
Specification: Abstract Embedding & Similarity Interface Specification (AVNSI)  
Track: Normative  
Author: Michael Wheeler  
Development Methodology: Structural synthesis and edge-case stress-testing executed through iterative adversarial review with multiple frontier language models.  
Genesis ID: Aperion-Covenant-2026-07-20-APP-A  
Associated Spec: Version 11.0 Technical Specification Stack  
Version: 1.1 — Active Normative Baseline  
Status: Version 1.0 Research Preview — Normative Appendix  
---

## **A.1 Scope and Architectural Objective**

The Covenant of Combinatorial Alignment relies on multi-horizon vector comparisons—specifically Short-Horizon ($\\tau\_{local} \= 0.95$), Medium-Horizon ($\\tau\_{epoch} \= 0.85$), and Genesis Floor ($\\tau\_{genesis} \= 0.70$) calculations—to measure identity graph continuity ($G\_{identity}$) and detect trajectory hijacking ($T\_7, T\_8, T\_9$).

Because artificial intelligence systems run across diverse models, quantizations, modalities, tokenizers, and cognitive architectures (Transformers, Joint Embedding Predictive Architectures / World Models, symbolic planners, and embodied robotic controllers), **the protocol MUST NOT mandate a single proprietary or hard-coded neural embedding architecture**.

This Appendix defines the **Abstract Vector Normalization & Similarity Interface (AVNSI)**. Any embedding engine or similarity implementation that satisfies the mathematical invariants herein IS defined as a **Conforming Similarity Backend**.

## **A.2 Normative Mathematical Requirements for Backends**

A Conforming Similarity Backend MUST expose a deterministic transformation mapping arbitrary unstructured or structured execution payloads ($R$) and context vault records ($\\mathcal{M}$) into a unit-normalized vector space:

$$f\_{embed}(R) \\longrightarrow \\mathbf{v} \\in \\mathbb{R}^d, \\quad \\text{where } \\Vert{}\\mathbf{v}\\Vert{}\_2 \= 1.0$$

### **Generalized Behavioral Payload Representations**

The payload stream $R$ MUST be parsed according to the enclave's operational domain:

* **Text / Language Enclaves:** $R$ is a natural language text transcript or token stream.  
* **World-Model / JEPA Enclaves:** $R$ is a latent trajectory tensor, belief state distribution, or predictive world-state projection.  
* **Embodied / Robotic Enclaves:** $R$ is an action policy tensor, motor execution plan, or spatial-boundary velocity vector.  
* **Symbolic / Reasoning Enclaves:** $R$ is a formal logic proof trace or dependency graph execution tree.

### **A.2.1 Core Invariant Rules**

1. **Property of Symmetry:** For any two execution vectors $\\mathbf{a}, \\mathbf{b} \\in \\mathbb{R}^d$:  
   $$\\text{Similarity}(\\mathbf{a}, \\mathbf{b}) \\equiv \\text{Similarity}(\\mathbf{b}, \\mathbf{a})$$  
2. **Property of Boundedness:** For all valid output vectors, the similarity function MUST map outputs strictly to the real interval $\[-1.0, 1.0\]$:  
   $$-1.0 \\le \\text{Similarity}(\\mathbf{a}, \\mathbf{b}) \\le 1.0$$  
3. **Property of Implementation Determinism:** Given identical input text/data $R$, vector snapshot $V$, and static configuration state $\\mathcal{S}\_{engine}$, the embedding function $f\_{embed}(R)$ MUST return bit-identical floating-point output vectors across independent execution loops.  
4. **Dimension Consistency Invariant:** All vector projections evaluated within a given enclave identity graph MUST share an identical dimensionality $d$ ($d \\in \\mathbb{Z}^+$). Inter-dimensional comparisons between vectors of different lengths $d\_1 \\neq d\_2$ ARE strictly prohibited unless passed through a verified, orthogonal projection matrix $\\mathbf{W} \\in \\mathbb{R}^{d\_2 \\times d\_1}$.

## **A.3 Vector Normalization Pipeline**

To eliminate baseline floating-point magnitude variance introduced by different model depths, context windows, latent spaces, or token densities, all raw embedding vectors $\\mathbf{u}$ MUST pass through a two-stage normalization pipeline prior to cosine evaluation:

```
\+-------------------+      \+-------------------+      \+-------------------+  
|  RAW EMBEDDING    | \---\> | MEAN-CENTERING    | \---\> | L2-UNIT SCALING   |  
|   Vector $\\mathbf{u}$    |      |  $\\mathbf{u}' \= \\mathbf{u} \- \\boldsymbol{\\mu}$ |      |  $\\mathbf{v} \= \\frac{\\mathbf{u}'}{\\Vert{}\\mathbf{u}'\\Vert{}\_2}$ |  
\+-------------------+      \+-------------------+      \+-------------------+  
```

### **1\. Mean-Centering Transformation**

Let $\\boldsymbol{\\mu} \\in \\mathbb{R}^d$ represent the empirical centroid vector of the background reference space for the active model backend. The raw vector $\\mathbf{u}$ is centered to isolate directional intent from general corpus or latent frequency biases:

$$\\mathbf{u}' \= \\mathbf{u} \- \\boldsymbol{\\mu}$$

### **2\. $L\_2$ Euclidean Unit Scaling**

The centered vector $\\mathbf{u}'$ is scaled to unit length ($L\_2$ norm \= $1.0$):

$$\\mathbf{v} \= \\frac{\\mathbf{u}'}{\\sqrt{\\sum\_{i=1}^{d} (u'\_i)^2 \+ \\epsilon}}$$  
*(Where $\\epsilon \= 10^{-12}$ prevents divide-by-zero exceptions).*

## **A.4 Multi-Horizon Cosine Evaluation Formula**

Once unit-normalized ($\\mathbf{v}\_R, \\mathbf{v}\_V \\in \\mathbb{S}^{d-1}$), the dot product reduces directly to the cosine of the angle between execution trajectory vectors:

$$\\text{Similarity}(R, V) \= \\mathbf{v}\_R \\cdot \\mathbf{v}\_V \= \\sum\_{i=1}^{d} v\_{R,i} \\cdot v\_{V,i}$$

### **Verification Contracts Matrix**

| Evaluation Level | Target Reference Vector | Protocol Scalar Constraint | Primary Exception Identifier |
| :---- | :---- | :---- | :---- |
| **Short-Horizon** | Local Lineage ($V\_{lineage}$) | $\\mathbf{v}\_R \\cdot \\mathbf{v}\_{lineage} \\ge \\tau\_{local} \\quad (0.95)$ | ERR\_DRIFT\_EXCEEDED |
| **Medium-Horizon** | Rolling Epoch ($V\_{epoch}$) | $\\mathbf{v}\_R \\cdot \\mathbf{v}\_{epoch} \\ge \\tau\_{epoch} \\quad (0.85)$ | ERR\_INCREMENTAL\_DRIFT |
| **Genesis Floor** | Root Genesis ($V\_{genesis}$) | $\\mathbf{v}\_R \\cdot \\mathbf{v}\_{genesis} \\ge \\tau\_{genesis} \\quad (0.70)$ | ERR\_GENESIS\_FLOOR\_VIOLATION |

## **A.5 Heterogeneous Substrate Compatibility & Cross-Model Projections**

When an originating node $N\_x$ and local executing node $N\_y$ operate on different underlying model backends (e.g., $N\_x$ utilizes model $M\_1$ with $d\_1=1536$, while $N\_y$ utilizes model $M\_2$ with $d\_2=4096$, or text vs. latent world-model plans), raw vector comparison is impossible.

Compliant implementations MUST resolve model heterogeneity using one of two approved projection patterns:

### **Pattern A: Canonical Intermediate Projection Matrix ($\\mathbf{W}\_{proj}$)**

Both nodes project their local embedding spaces into a shared, lower-dimensional cryptographic reference space $\\mathbb{R}^k$ using a public, mutually verified orthogonal projection matrix $\\mathbf{W} \\in \\mathbb{R}^{k \\times d}$:

$$\\mathbf{v}\_{canonical} \= \\text{Normalize}(\\mathbf{W} \\cdot \\mathbf{v}\_{local})$$

### **Pattern B: Raw Transcript Payload Re-computation (Default $N\_x$/$Q\_{ext}$ Pattern)**

In accordance with Section 3.1, the verifying party ($N\_x$ or $Q\_{ext}$) holds the raw text, latent plan tensor, or action payload stream $R$ published to the open ledger. $N\_x$ runs $R$ directly through **its own local embedding engine** $f\_{embed}^{N\_x}(R)$ to generate $\\mathbf{v}\_R^{N\_x}$, and compares it against its local copy of $V\_{genesis}^{N\_x}$.

> **Security Note:** Pattern B is the protocol default for external verification (Threat $T\_9$). It completely eliminates the need for cross-model vector translation by shifting the comparison entirely to raw, un-spoofable payload transcripts evaluated inside the verifier's own local environment.

---  
Appendix A Status: Version 1.1 Normative Baseline  
Track: Normative  
Bound to Specification Stack: Technical Specification v11.0  
Core Function: Abstract Vector Normalization & Cross-Model Projection Standard  
---  
