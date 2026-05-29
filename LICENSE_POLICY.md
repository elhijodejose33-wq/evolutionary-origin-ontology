# LICENSE_POLICY.md

## License Boundary and Rights Policy

> **Correct naming applies to rights, authorship, and licensing too.**
>
> This repository must not claim more freedom over source-derived material than the source author has granted.

⸻

## 1. Source Text License

The source text *El hijo de José* states that it is licensed under:

```text
Creative Commons Atribución–No Comercial (CC BY-NC)
```

It allows copying, sharing, and distribution with attribution and prohibits commercial use without the author’s explicit written consent.

Because the source text does not specify a Creative Commons version in the parsed license notice, repository metadata should avoid falsely asserting a specific version unless the rights holder clarifies it.

Recommended metadata treatment:

```yaml
license: other
license_name: "Creative Commons Attribution–NonCommercial (CC BY-NC; version unspecified in source notice)"
```

⸻

## 2. Repository License Boundary

This project may contain multiple legal categories.

| Material | Recommended Treatment |
|---|---|
| Original code written for this repository | CC0 1.0 Universal, if the maintainer owns it and wants public-domain dedication. |
| General repository scaffolding | CC0 1.0 Universal, if not source-derived. |
| Dataset entries derived from the source framework | CC BY-NC terms inherited from the source unless separately relicensed by the rights holder. |
| Documentation that closely paraphrases the source ontology | Treat as source-derived and non-commercial unless separately authorized. |
| Direct quotations from the book | Use only with attribution and within the source license terms. |
| Commercial use of source-derived material | Requires explicit written permission from the rights holder. |

⸻

## 3. Why This Matters

The ontology itself teaches that false names stabilize false systems.

A repository that calls non-commercial source-derived material “public domain” when it is not would reproduce the very Inversion the framework exists to expose.

Therefore:

```text
Do not use CC0 to erase the author’s retained non-commercial restriction.
Do not use open-source aesthetics to override source rights.
Do not confuse shareability with commercial permission.
```

⸻

## 4. Suggested Repository Layout

```text
.
├── LICENSE                  # CC0 for eligible original code/tooling only
├── LICENSE_POLICY.md         # Explains the boundary
├── NOTICE.md                 # Optional attribution and source-rights notice
├── data/
│   └── evolutionary-origin-ontology.jsonl  # Source-derived; non-commercial unless authorized
└── src_or_tools/
    └── original_code.py       # Eligible for CC0 if maintainer owns it
```

⸻

## 5. Suggested Notice for Source-Derived Dataset

```text
This dataset is derived from the philosophical framework of El hijo de José.
The source text is licensed under Creative Commons Attribution–NonCommercial
(CC BY-NC; version unspecified in the source notice). Commercial use of
source-derived material requires explicit written permission from the rights
holder.
```

⸻

## 6. Maintainer Action Items

Before publication, confirm:

| Item | Required Action |
|---|---|
| Source rights | Verify whether the author wants CC BY-NC 4.0, CC BY-NC unspecified, or another license label. |
| Dataset license | Set Hugging Face metadata to `other` unless version is clarified. |
| Code license | Keep CC0 only for code/tooling the maintainer owns. |
| Commercial restriction | Make non-commercial status visible in README and dataset card. |
| Attribution | Include author/project citation in `CITATION.cff`. |

⸻

## 7. Final Licensing Principle

```text
Life must circulate truthfully.

So must rights.

If a license boundary exists, name it.
If permission is limited, preserve it.
If attribution is required, give it.
If commercial use is prohibited, do not disguise it as open access.
```
