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

# INFERENCE RULES — Zanistarast Deductive System (v1)

Amaç:
Sistemin nasıl akıl yürüttüğünü açıkça tanımlamak.

Bu kurallar olmadan teoremler yalnızca iddia olur.
Kurallar sistemi matematiksel hale getirir.

---

## R1 — Katman Yükseltme Kuralı

Eğer bir varlık Dn boyutunda tanımlıysa,
ve Dn+1 onu kapsıyorsa,
o zaman projeksiyon mümkündür.

dim(x)=Dn ∧ Dn ⊂ Dn+1
⇒ proj_Dn(x) tanımlıdır

---

## R2 — Çelişki Eliminasyonu

(x ∧ ¬x) ⇒ ⊥

Çelişkili kümeden normatif hüküm türetilemez.

---

## R3 — Normatif Üretim Kuralı

Normatif sonuç için ★ gerekir.

★(D5, D6) ⇒ 𝕁

Ahlak ve hüküm birlikte değilse bağlayıcı karar üretilemez.

---

## R4 — Onay Zinciri

Know(x) ⇒ ∃y : Confirm_y(x)

Tek onay kanalı bilgi statüsü üretmez.

---

## R5 — Alt Boyut Sabitleme Tehlikesi

dim(system) ⊆ {D1, D2}
⇒ normatif üretim imkânsız

---

## R6 — Tip Güvenliği

Eğer bir ifade tip kurallarını ihlal ederse,
o ifade geçersizdir.

TypeError(x) ⇒ ⊥

---
