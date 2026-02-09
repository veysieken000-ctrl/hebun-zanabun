# OPERATORS — Typing & Semantics (v1)

Amaç: “⊗ ne demek?” tartışması bitmeli.

## 1) Tip Sistemi (özet)
- 𝔹: varlık
- 𝕂: bilgi nesnesi
- 𝕍: değer/ahlak kısıtları
- 𝔻₆: boyut etiketi

## 2) Operatörler

### ⊕ (merge)
- Tip: (T × T) → T
- Anlam: aynı tipte iki nesnenin tek temsil altında birleşmesi.
- Örn: iki bilgi kaynağının ortaklaştırılması.

### ⊗ (composition)
- Tip: (A × B) → C (C bağlama göre)
- Anlam: “iki farklı katman” etkileşimi ile yeni yapı üretir.
- Örn: (bilgi ⊗ değer) → normatif karar

### ◁ (normlama)
- Tip: (𝕂 × 𝕍) → 𝕂
- Anlam: bilgi, değer kısıtlarıyla sınırlandırılır; ‘keyfi bilgi’ engellenir.

### ★ (dual-lock: Ahlak + Hüküm)
- Tip: (karar × (ahlak,hüküm)) → bağlayıcı-sonuç
- Anlam: Ahlak ve hükmün birlikte kilitleyici olması (ikili sistem gereği).

## 3) Yasaklar
- Tip uyuşmazlığına izin yok.
- Aynı sembol iki farklı işlemde kullanılmaz.
3) Tip sistemi (x nedir? varlık mı? bilgi mi?)

# OPERATORS — Formal Operator Definitions (v1)

Amaç:
İşlemler matematiksel netlikte.

---

## ⊕ (Merge)

Tip: (T × T) → T  
Aynı tip birleşimi.

---

## ⊗ (Composition)

Tip: (A × B) → C  
Katmanlar arası üretim.

Örnek:
Bilgi ⊗ Değer → Normatif yapı

---

## ◁ (Normlama)

Tip: (𝕂 × 𝕍) → 𝕂  
Bilgi, değer filtresinden geçirilir.

---

## ★ (Dual Lock)

Tip: (Ahlak × Hüküm) → Binding

İkili sistem gereği:
Ahlak + Hüküm birlikte bağlayıcıdır.

---

## Yasak

- Tip dışı işlem yok.
- Aynı sembol iki işlemde kullanılmaz.
Buraya kadar temel formal çekirdek tamamlandı.

# OPERATORS — Operator Semantics (v1)

Amaç: Sembollerin “hangi tür işlem” olduğunu sabitlemek.

## 1) ⊗ (Birleşim/kompozisyon)
- Tip: (Type-level composition)
- Kullanım: 𝕂 ⊗ 𝕍
- Anlam: Bilgi (𝕂) ile değer/aksiyoloji (𝕍) birleşmeden normatif bağlayıcılık doğmaz.

## 2) ★ (İkili Kilit / Dual Lock)
- Tip: (Kilit operatörü)
- Kullanım: (Ahlak ★ Hüküm) ⇒ 𝕁
- Anlam: Ahlak tek başına “iyi niyet” üretir ama bağlayıcı düzen üretmez.
  Hüküm tek başına “güç/karar” üretir ama adalet garantisi vermez.
  ★ birlikteyken bağlayıcı norm (𝕁) üretir.

## 3) proj_d(x) (Projeksiyon)
- Tip: fonksiyon
- Kullanım: proj_3(x) = x’in zihin boyutundaki görünümü
- Not: projeksiyon “indirgeme” değildir; sadece görünüm alır.

## 4) Confirm_y(p)
- Tip: doğrulama operatörü (epistemik kontrol)
- Kullanım: Know(p) ⇒ ∃y Confirm_y(p)
# OPERATORS — Semantic Operator Definitions (v1)

Amaç:
Zanistarast formal yapısında kullanılan tüm operatörlerin
matematiksel ve semantik anlamını netleştirmek.

Bu dosya sembollerin yalnızca adını değil,
mantıksal davranışını tanımlar.

---

## 1) Mantıksal Operatörler

### → (İmplikasyon)

Tanım:
p → q ≡ ¬p ∨ q

Anlam:
p doğru ise q zorunludur.
Zanistarast’ta boyut geçişlerinde sık kullanılır.

---

### ∧ (Konjonksiyon)

p ∧ q yalnızca her ikisi doğruysa doğrudur.

Normatif bağlayıcılık için
Ahlak ∧ Hüküm birlikte gerekir.

---

### ∨ (Disjunction)

p ∨ q en az biri doğruysa doğrudur.

---

### ¬ (Negation)

¬p → p doğru değildir.

---

### ⊥ (Çelişki)

p ∧ ¬p ⇒ ⊥

Çelişki oluşursa sistem bilgi üretmez.

---

## 2) Zanistarast Özgü Operatörler

---

### ★ (Dual Binding Operator)

Tanım:

★(A,H) ⇒ 𝕁

Burada:

A = Ahlak bileşeni  
H = Hüküm bileşeni  
𝕁 = Bağlayıcı normatif sonuç

Kural:
★ olmadan bağlayıcılık yoktur.

Semantik anlam:
Tek taraflı norm üretilemez.
Ahlak tek başına yeterli değildir.
Hüküm tek başına yeterli değildir.

---

### ⊗ (Gerekli Birleşim)

Tanım:

(𝕂 ⊗ 𝕍)

𝕂 = Bilgi
𝕍 = Değer

Anlam:
Normatif üretim için hem bilgi hem değer gerekir.
Salt bilgi norm üretmez.

---

### ⟂ (Ontolojik Karşıtlık)

x ⟂ y

Anlam:
x, y olmadan görünür hale gelmez.

Örnek:
iyi ⟂ kötü
varlık ⟂ yokluk

Bu operatör ontolojik dualiteyi ifade eder.

---

## 3) Fonksiyonel Operatörler

---

### dim(x)

x’in boyutunu verir.

dim : 𝔹 → 𝔻₆

---

### proj_d(x)

x’in d boyutuna izdüşümünü verir.

proj_d : 𝔹 → 𝔹

Kural:
proj_d(x) alt boyuta indirgeme değildir,
yalnızca izdüşümdür.

---

### Confirm_y(p)

y’nin p iddiasını onaylaması.

Confirm : Agent × Claim → {0,1}

İki-Bilen şartının formel operatörüdür.

---

## 4) Meta-Kural

Hiçbir özel operatör
mantıksal çelişki üretmeyecek şekilde tanımlanmıştır.

★, ⊗, ⟂ operatörleri
standart mantıkla uyumlu genişletilmiş semantik operatörlerdir.

---

Sonuç:
Bu dosya,
Zanistarast’ın “sezgisel değil,
operatör-semantik temelli” olduğunu gösterir.

