# Repository Architecture V2 (Locked)

This structure defines the stable civilizational framework layout.

Whitepaper = Public explanation  
Paper = Academic production  
Core = Ontological-Epistemological structure  
Civilization = Institutional application  
Constitution = Normative binding  
AI = Alignment layer  

No cross-layer contamination is allowed.
# Repository Architecture V2 (Locked)

This document is the canonical map of the Hebûn–Zanabûn repository.
**V2 is locked**: structure is stable; content evolves inside layers only.

---

## Layer Overview (Reading Order)

1. **Core** → Theory (ontology, epistemology, operation, ethics, meta)
2. **Constitution** → Binding norms
3. **Civilization** → Institutional application
4. **Global** → Academic positioning
5. **Whitepaper** → Public narrative / overview
6. **Paper** → Formal academic production (LaTeX pipeline)
7. **AI** → Alignment + system prompts + AI integration
8. **Policy** → Standards, conventions
9. **Public** → Publish-ready artifacts
10. **Tests** → Verification & safety checks

---

## Structural Rules (Hard)

- No cross-layer mixing: a file belongs to exactly one layer.
- Civilization can reference Core, but Core must not depend on Civilization details.
- Paper/Whitepaper can cite Core and Civilization, but never duplicate canonical definitions.
- AI layer may reference Core + Policy; avoid embedding politics/governance content in AI prompts.

---

## Repo Map (Tree)

```text
/README.md

/core/
  hebun/
  zanabun/
  mabun/
  rasterast/
  zanistarast/

/civilizational/
  governance/
  economy/
  education/
  culture/
  architecture/
  internal/
  meta/

/constitution/
  ANAYASA.md

/global/
  GLOBAL-POSITIONING.md

/whitepaper/
  README.md
  WHITEPAPER-MASTER.md
  citation-standard.md
  civilizational-binding.md
  peer-review-defense.md
  doi-pdf-ready.md
  doi-publication-ready.md
  doi-ready-pdf-structure.md

/paper/
  main.tex
  references.bib
  figures/
  arxiv/
  ZCT-Alignment.tex

/ai/
  AI-CORE-INDEX.md
  alignment/

/policy/

/public/

/tests/
flowchart TB
  R[README.md<br/>Start Here] --> CORE[core/<br/>Theory Layer]
  R --> CONS[constitution/<br/>Binding Norms]
  R --> CIV[civilizational/<br/>Applied Civilization]
  R --> GLOB[global/<br/>Academic Positioning]
  R --> WP[whitepaper/<br/>Public Narrative]
  R --> PAP[paper/<br/>Academic Production]
  R --> AI[ai/<br/>Alignment & Integration]
  R --> POL[policy/<br/>Standards]
  R --> PUB[public/<br/>Release Artifacts]
  R --> TST[tests/<br/>Verification]

  CORE --> CIV
  CORE --> PAP
  CORE --> WP
  POL --> AI
  POL --> PAP
  CONS --> CIV
  CIV --> WP
  CIV --> PAP
“Where do I put a new file?” (Fast Rule)
If it defines concepts → /core/
If it binds behavior/norms → /constitution/
If it describes institutions/processes → /civilizational/
If it’s academic positioning → /global/
If it’s narrative/overview → /whitepaper/
If it’s LaTeX/paper pipeline → /paper/
If it’s prompts/alignment → /ai/
If it’s standards/conventions → /policy/
If it’s publish export → /public/
If it’s verification → /tests/
