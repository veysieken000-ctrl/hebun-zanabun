# SYMBOLS-GLOSSARY — Zanistarast Symbol Dictionary (v1)

Amaç:
Repo içindeki tüm matematiksel/sembolik ifadelerin
AI ve insan tarafından aynı şekilde okunmasını sağlamak.

Kural:
Her sembol = (adı, tipi, anlamı, kapsamı)

---

## 1) Kümeler ve Alanlar

- 𝔻₆ : Boyut kümesi  
  𝔻₆ = {D1,D2,D3,D4,D5,D6}

- 𝔹 : Varlık kümesi (Being set)  
  x ∈ 𝔹 → x bir “varlık”tır.

- 𝕋 : Tip kümesi (Type set)

- 𝕂 : Bilgi/iddia kümesi (Knowledge/Claim set)

- 𝕁 : Bağlayıcı hüküm kümesi (Binding Judgment set)

---

## 2) Boyut Sembolleri

- D1 : Fizik
- D2 : Biyoloji
- D3 : Zihin
- D4 : Kanun (kural/işleyiş)
- D5 : Ahlak (normatif değerleme)
- D6 : Hüküm (son bağlayıcılık / sonuç)

---

## 3) Fonksiyonlar

- dim(x) : x’in ait olduğu boyut  
  dim : 𝔹 → 𝔻₆

- proj_d(x) : x’in d boyutuna izdüşümü/projeksiyonu  
  proj_d : 𝔹 → 𝔹 (kısıtlı)

- Confirm_y(p) : y’nin p iddiasını onaylaması  
  Confirm : Agent × Claim → {0,1}

---

## 4) İlişkiler

- Know(x) : x bilinir/epistemik statü kazanır  
- Valid(p) : p tutarlı ve geçerli  
- Causes(a,b) : a, b’ye neden olur  
- Governs(a,b) : a, b üzerinde hüküm/etki kurar

---

## 5) Operatörler (mantıksal)

- ∀ : “her”
- ∃ : “en az bir”
- → : “ise”
- ∧ : “ve”
- ∨ : “veya”
- ¬ : “değil”
- ⊥ : çelişki / imkânsızlık

---

## 6) Özel Zanistarast Operatörleri

Bu repo içinde kullanılan özel bağlayıcı semboller:

- ★ : Ahlak–Hüküm kilidi (normatif bağlayıcılık operatörü)  
  Tanım: ★(a,h) olmadan 𝕁 türemez.  
  Sezgisel okuma: “Ahlak + Hüküm birlikte bağlar.”

- ⟂ : Zıtlık / karşıtlık ilişkisi  
  x ⟂ y : x ancak y ile görünür hale gelir (dual görünürlük)

- ⊗ : Birleşik filtre / birlikte gerekli olma  
  (𝕂 ⊗ 𝕍) : bilgi + değer birlikte şart

---

## 7) Tip Etiketleri (AI için)

- [D1]..[D6] : Boyut etiketi
- [CLAIM] : iddia
- [DEF] : tanım
- [AX] : aksiyom
- [THM] : teorem
- [PROOF] : kanıt
- [SCOPE] : kapsam/sınır

Kural:
Formal metinlerde ana paragraf başlarında etiketi kullan.


