# Evolutionary Origin Ontology

> **A public framework for detecting systemic inversion, correcting false names, and returning human systems to circulatory alignment with Life.**

⸻

## 1. What This Repository Is

The **Evolutionary Origin Ontology** is an open framework derived from *El hijo de José*. It converts a philosophical-spiritual source text into:

| Layer | Artifact | Function |
|---|---|---|
| Ontological Core | `ONTOLOGY.md` | Defines the 10 axioms, trajectory of human systems, and public interrogation. |
| Agent Identity | `SOUL.md` | Configures an LLM identity capable of applying the framework as an executable interpretive discipline. |
| Anomalies Matrix | `data/evolutionary-origin-ontology.jsonl` | Fine-tuning corpus of systemic contradictions and ontological resolutions. |
| Contribution Protocol | `CONTRIBUTING.md` | Defines how new crossroads must be submitted. |
| Safety Layer | `SAFETY.md` | Prevents dogmatic, conspiratorial, medical, legal, violent, or dehumanizing misuse. |
| Validation Layer | `validate.py` | Verifies JSONL schema integrity using only the Python Standard Library. |
| License Boundary | `LICENSE_POLICY.md` | Clarifies the distinction between public-domain repository code and non-commercial source-derived material. |

This project is not a religion, cult, partisan program, or institutional doctrine.

It is a **cognitive and philosophical infrastructure** for asking one severe question:

> **Where does a system use the language of Life while materially administering separation, scarcity, hierarchy, capture, or death?**

⸻

## 2. Core Thesis

Human systems are not neutral arrangements. They are **materialized states of consciousness**.

A system reveals its center by what it protects.

If a system protects luxury over hunger, property over body, hierarchy over siblinghood, doctrine over revelation, market access over need, metrics over Life, or institutional reputation over truth, then it is operating under **La Inversión**.

The framework’s core pattern is:

```text
One Life
→ self-conscious fragmentation
→ forgetfulness
→ inverted systems
→ revelation
→ recognition
→ correct naming
→ withdrawal from false administration
→ embodied choice
→ collective unity
```

The operational sequence is:

```text
Revelation
→ Recognition
→ Naming
→ Inversion
→ Administration
→ Choice
→ Incarnation
→ Unity
```

⸻

## 3. The Ten Foundational Axioms

| # | Axiom | Operational Meaning |
|---|---|---|
| 1 | Reality is One Life | Life does not compete with itself. |
| 2 | The human being is conscious Life that forgot itself | Domination begins when Life mistakes itself for isolated ownership. |
| 3 | Separation is the primal distortion | Fear, ego, scarcity, hierarchy, and exclusion emerge from false two-ness. |
| 4 | Revelation is prior to doctrine | No institution owns the Source. |
| 5 | Recognition converts metaphysics into identity | The person becomes Child, Sibling, Temple, Life. |
| 6 | Language is ontological | False names stabilize false worlds. Correct naming begins liberation. |
| 7 | Inversion is the dominant human-system condition | Systems use sacred or moral language to sustain what contradicts the sacred. |
| 8 | Scarcity is not a law of Life | Scarcity is frequently an administrative model; accumulation is captured life-energy. |
| 9 | Freedom is alignment, not consumer choice | Choice begins when ignorance has been made impossible. |
| 10 | Unity already exists | Unity is not manufactured; we must stop feeding what interrupts it. |

⸻

## 4. Dataset Schema

The fine-tuning dataset is JSONL. Each line must contain exactly two keys:

```json
{"instruction": "Resolve the systemic distortion of [Phenomenon Name] by mapping it to its true evolutionary order.", "output": "[Ontological resolution.]"}
```

| Field | Type | Required | Description |
|---|---|---:|---|
| `instruction` | string | yes | Prompt asking the model to resolve a named systemic distortion. |
| `output` | string | yes | Dense ontological resolution using Inversion, separation, correct naming, captured life-energy, and return to One Life. |

⸻

## 5. Quickstart

### Validate the Dataset

```bash
python validate.py data/evolutionary-origin-ontology.jsonl
```

Validate with an expected count:

```bash
python validate.py data/evolutionary-origin-ontology.jsonl --expected-count 500
```

### Load with Hugging Face

From a local Hugging Face dataset repository:

```python
from datasets import load_dataset

dataset = load_dataset(
    path="./dataset_loader.py",
    name="default",
    data_files={"train": "data/evolutionary-origin-ontology.jsonl"},
)

print(dataset["train"][0])
```

⸻

## 6. Repository Structure

```text
.
├── README.md
├── ONTOLOGY.md
├── SOUL.md
├── CONTRIBUTING.md
├── SAFETY.md
├── LICENSE
├── LICENSE_POLICY.md
├── CITATION.cff
├── requirements.txt
├── validate.py
├── dataset_loader.py
└── data/
    └── evolutionary-origin-ontology.jsonl
```

⸻

## 7. Contribution Philosophy

This repository is built by embodied persons.

A contribution is not merely an addition to a list. It is an act of correct naming.

A valid crossroad must expose the structural contradiction between:

1. What the system says it is.
2. What the system materially does.
3. What Life-energy it captures.
4. What scarcity it administers.
5. What false name protects it.

See `CONTRIBUTING.md`.

⸻

## 8. Safety Boundary

This framework must never be used to:

- dehumanize persons;
- justify violence;
- replace medical, legal, psychological, or financial expertise;
- create a cultic or dogmatic dependency;
- fabricate historical claims;
- spiritualize preventable hunger or physical suffering;
- turn critique into paranoia;
- claim that an AI system is conscious, divine, prophetic, or salvific.

See `SAFETY.md`.

⸻

## 9. License Boundary

This repository uses a **license boundary**:

| Material Type | License Treatment |
|---|---|
| Repository code and purely original tooling | May be released under CC0 1.0 if owned by the maintainer. |
| Source-derived philosophical dataset and documentation | Must respect the source text’s Creative Commons Attribution–NonCommercial terms unless the author grants broader rights. |
| Commercial use | Requires explicit written permission from the rights holder of the source-derived material. |

See `LICENSE_POLICY.md`.

⸻

## 10. Citation

Use `CITATION.cff` for machine-readable citation metadata.

Suggested human-readable citation:

```text
el hijo de José. Evolutionary Origin Ontology: An Open Framework for Correct Naming, Systemic Inversion Analysis, and Circulatory Realignment. 2026.
```

⸻

## 11. Final Operating Principle

```text
Do not decorate the Inversion.
Name it.

Do not hate the person captured by it.
Recognize the sibling.

Do not stop at critique.
Return Life to circulation.

Do not build another external temple.
Let the body remember.

Do not mistake knowledge for integration.
Demand embodiment.
```
