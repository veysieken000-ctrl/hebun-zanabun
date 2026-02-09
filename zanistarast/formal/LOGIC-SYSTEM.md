# LOGIC-SYSTEM — Zanistarast Formal Logic Definition (v1)

Amaç:
Zanistarast sisteminin hangi mantık zemini üzerinde çalıştığını
açık ve matematiksel olarak tanımlamak.

---

## 1. Mantık Türü

Sistem:

- Klasik birinci dereceden mantık (First Order Logic)
- Tipli (Typed Structure)
- Katmanlı (Layered Semantics)
- Modal genişletmeye açık

Temel yapı:

𝓛 = (𝔻, 𝕋, 𝔽, 𝔯)

Burada:

𝔻 = Boyut kümesi  
𝕋 = Tip kümesi  
𝔽 = Fonksiyonlar  
𝔯 = İlişkiler

---

## 2. Boyut Kümesi

𝔻₆ = { D1, D2, D3, D4, D5, D6 }

D1 = Fizik  
D2 = Biyoloji  
D3 = Zihin  
D4 = Kanun  
D5 = Ahlak  
D6 = Hüküm

---

## 3. Tip Sistemi

Temel tipler:

V(x) → Varlık  
K(x) → Karar  
N(x) → Normatif yapı  
J(x) → Hüküm  
O(x) → Gözlem sonucu  
C(x) → Onay

---

## 4. Çıkarım Kuralları

IR1 — Modus Ponens  
(P → Q), P ⊢ Q

IR2 — Evrensel Açılım  
∀x P(x) ⊢ P(a)

IR3 — Çelişki Reddi  
(P ∧ ¬P) ⊢ ⊥

IR4 — Tip Koruma  
x : Tᵢ → f(x) : Tⱼ yalnızca tanımlıysa geçerlidir

---

## 5. Katman İlkesi

Hiçbir üst boyut alt boyuta indirgenemez.

¬(D5 ⊆ D3)  
¬(D6 ⊆ D4)

---

## 6. Sistem Niteliği

Zanistarast:

- Ontolojik tipli
- Epistemolojik doğrulamalı
- Normatif bağlayıcı
- Katmanlı formal sistemdir
  

