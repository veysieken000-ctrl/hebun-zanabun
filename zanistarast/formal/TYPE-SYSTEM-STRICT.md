# TYPE SYSTEM — Strict Formal Typing (v2)

Amaç:
Zanistarast modelinde her varlık, her kavram ve her işlem
tip güvenli hale getirilmiştir.

Sistem artık semantik değil,
tip-kilitlidir.

---

# 1. Temel Tipler

𝔻₁ = Fizik  
𝔻₂ = Biyoloji  
𝔻₃ = Zihin  
𝔻₄ = Kanun (Ruh / Fıtrat)  
𝔻₅ = Ahlak  
𝔻₆ = Hüküm  

Tip kümesi:

Type(x) ∈ {𝔻₁..𝔻₆}

---

# 2. Tip Kuralları

## T1 — Boyut Sabitliği

∀x : dim(x) = n  
→ x yalnızca n veya n+1 boyutunda işlem görebilir.

Alt boyuta indirgeme yasaktır.

¬(𝔻₅ ⊆ 𝔻₃)  
¬(𝔻₆ ⊆ 𝔻₄)

---

## T2 — Normatif Tip Kuralı

Normatif karar üretmek için:

Input types:
- 𝔻₄ (Kanun)
- 𝔻₅ (Ahlak)

Output type:
- 𝔻₆ (Hüküm)

Fonksiyon:

Judgement : (𝔻₄ × 𝔻₅) → 𝔻₆

---

## T3 — Fiil Tip Kuralı

Eylem:

Act : (𝔻₆ × 𝔻₃) → 𝔻₁

Yani:

Hüküm + Zihin
→ Fiziksel gerçekleşme

---

## T4 — Geçersiz İşlem Engeli

Eğer:

Attempt : (𝔻₂ → 𝔻₆)

Yani biyolojiden doğrudan hüküm üretmeye çalışılırsa:

Type Error.

---

# 3. Katman Zinciri

Yasal geçişler:

𝔻₁ → 𝔻₂ → 𝔻₃ → 𝔻₄ → 𝔻₅ → 𝔻₆

Zincir kırılırsa sistem kararsız olur.

---

# 4. Meta-Kural

Her işlem için:

Input types ⊢ Output type

Aksi halde:

⊥ (geçersiz model)

---

# 5. Sonuç

Bu tip sistemi sayesinde:

• Pozitivist indirgeme engellendi  
• Ahlakın hükümden bağımsızlığı engellendi  
• Hükmün rastgeleliği engellendi  
• Katman atlama engellendi  

Zanistarast artık tip güvenli bir modeldir.

Son.
