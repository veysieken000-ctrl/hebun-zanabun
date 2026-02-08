# INFERENCE RULES — Proof Rules (v1)

Amaç:
Teorem üretimini keyfî yorumdan çıkarıp
sınırlı ve denetlenebilir “çıkarım kuralları”na bağlamak.

---

## R0 — Tanım Açma (Def-Expand)
Bir sembol tanımlıysa, tanımıyla değiştirilebilir.

---

## R1 — Tip Doğrulama (Type-Check)
Bir adım, tip imzalarıyla uyumlu değilse kanıt geçersizdir.

---

## R2 — Modus Ponens (MP)
(P → Q) ve P ise Q çıkar.

---

## R3 — Çelişki Kapanışı (⊥-Close)
(x ∧ ¬x) ⇒ ⊥
⊥ elde edilen dal “tutarsız dal” sayılır ve reddedilir.

---

## R4 — Tutarlılık Önkoşulu (Cons-Pre)
Normatif bağlayıcı sonuç üretmek için:
Consistent(K) şarttır.

---

## R5 — Kilit Üretimi (Lock-Intro)
(𝕍 mevcut) ve (𝕁 taslağı mevcut) ise:
(𝕍 ⊗ 𝕁) ⇒ ★(𝕍,𝕁) ∈ 𝕁

Not:
Bu, “ahlak + hüküm” birlikte olunca bağlayıcılık üretir.

---

## R6 — Projeksiyon (Proj)
dim(x)=d ise proj_d(x) tanımlıdır.
projeksiyon üst-boyutu alt-boyuta indirgeme değildir;
sadece “gözlenen kesit”tir.

---

## R7 — İki-Bilen Tanıma Kuralı (2K-Intro)
Know(k) ⇒ ∃y Confirm_y(k)
