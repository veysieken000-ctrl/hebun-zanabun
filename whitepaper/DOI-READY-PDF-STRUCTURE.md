# DOI-ready PDF Structure (White Paper Packaging)

Müdebbir: Veysi yê MALA SAF  
Version: v1.2  

---

## Goal
Create a single PDF-ready “master paper” structure
that can be assigned a DOI later (Zenodo, OSF, institutional repository).

This file defines:
- Required sections
- File layout
- Metadata fields
- Export checklist

---

## 1) Master File (Single Source of Truth)
Create a master markdown:

/whitepaper/WHITEPAPER.md

It will include:
- Abstract
- Keywords
- Introduction
- System Overview
- Formal layer summary
- Axioms + theorems references
- Applications (Rasterast + Mabûn)
- Criticism-response
- Conclusion
- References

---

## 2) Required Metadata (for DOI platforms)
Include at top of WHITEPAPER.md:

- Title
- Subtitle
- Version
- Date
- Author role: Müdebbir
- Repository URL
- License
- Keywords (10–15)
- Abstract (150–250 words)

---

## 3) PDF Export Target
Export outputs to:

/whitepaper/releases/

Naming rule:
Hebun-Zanabun_WhitePaper_v1.2.pdf

---

## 4) Minimal Section Order (DOI-ready standard)

1. Title Page
2. Abstract
3. Keywords
4. Table of Contents (optional)
5. Introduction
6. Motivation / Problem Statement
7. Ontology (Hebûn)
8. Epistemology (Zanabûn)
9. Civilizational Layer (Rasterast + Mabûn)
10. Formal Layer (Axioms, Types, Theorems)
11. Criticism & Response (defensive layer)
12. Conclusion
13. References
14. Appendices (formal proofs)

---

## 5) References & Citation Policy
Create:

/whitepaper/REFERENCES.md

Rules:
- Every major claim must cite either:
  a) internal formal statement (A#, T#), or
  b) external academic reference, or
  c) Qur’anic/dini reference (if used) clearly marked as theological source.

---

## 6) Export Checklist (ready to publish)

- [ ] WHITEPAPER.md complete
- [ ] ABSTRACT present
- [ ] KEYWORDS present
- [ ] Version tag consistent everywhere (v1.2)
- [ ] Formal layer linked
- [ ] License included
- [ ] Repository URL included
- [ ] PDF export created under /whitepaper/releases/

---

## Next Step
After this, we build:

/whitepaper/WHITEPAPER.md
and connect every module into it.
