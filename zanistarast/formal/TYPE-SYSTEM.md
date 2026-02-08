# TYPE SYSTEM — Zanistarast Dimensional Typing (v1)

Amaç:
Sistem sembolik olarak çalışabilsin.
Her varlık, bilgi ve normatif ifade tip disiplinine bağlı olsun.
Tip ihlali = kanıt ihlali.

---

## 1) Temel Tipler

𝔹 : Being (Varlık taşıyıcıları)  
𝕂 : Knowledge object (Bilgi nesnesi)  
ℕ𝕆 : Normative Output (Bağlayıcı normatif sonuç)  
𝔻 : Dimension index (1..6)

---

## 2) Boyut Tipi

dim : 𝔹 → 𝔻

Her varlık en az bir boyut indeksine sahiptir.

A1 ile uyumlu:
∀x ∈ 𝔹, ∃d ∈ 𝔻 : dim(x)=d

---

## 3) Katman Projeksiyon Fonksiyonu

proj_d : 𝔹 → 𝔹

Bir varlık daha alt boyuta projekte edilebilir.
Ancak:

Üst boyut ⊄ Alt boyut

Bu, A2 ile tutarlıdır.

---

## 4) Normatif Üretim Fonksiyonu

★ : (𝔹₅ × 𝔹₆) → ℕ𝕆

Ahlak (5) ve Hüküm (6) birlikte normatif çıktı üretir.

Tek başına:
𝔹₅ ↛ ℕ𝕆  
𝔹₆ ↛ ℕ𝕆  

---

## 5) Bilgi Tip Disiplini

know : 𝔹 → 𝕂

confirm : (𝔹 × 𝕂) → Bool

A5 ile uyumlu:
Know(x) ⇒ ∃y : confirm(y, know(x)) = true

Tek doğrulama kanalı bilgi statüsü üretmez.

---

## 6) Çelişki Kontrolü

⊥ : inconsistency marker

Eğer:
p ∧ ¬p

ise:

System state = ⊥  
Normative production disabled.

---

## 7) Tip İhlali Kuralı

Eğer bir teorem:

𝔹 → ℕ𝕆

üretmeye çalışıyorsa ve ★ operatörü yoksa,

Bu çıkarım geçersizdir.

---

## 8) Sistem Güçlendirme

Bu tip sistemi sayesinde:

- Metafor = model olamaz
- İndirgeme = tip dönüşümü olmadan yapılamaz
- Normatif karar = zorunlu iki boyutlu kapıdan geçer

Bu dosya, aksiyomları “mantıksal çerçeveye” sabitler.

# TYPE SYSTEM — Zanistarast Layered Formal Types (v1)

Amaç:
Sistem içi kavram karışmasını engellemek.
Her sembolün matematiksel tipini belirlemek.

---

## 1. Temel Tip Kümeleri

𝔹 = Varlık kümesi  
𝔻₆ = {1,2,3,4,5,6} (Boyut kümesi)  
𝕂 = Bilgi kümesi  
𝕍 = Değer (ahlak) kümesi  
ℍ = Hüküm kümesi  
𝕁 = Normatif karar kümesi  

---

## 2. Tip Tanımları

dim : 𝔹 → 𝔻₆  
Know : 𝔹 → 𝕂  
Value : 𝔹 → 𝕍  
Judge : (𝕂 × 𝕍) → ℍ  
Bind : ℍ → 𝕁  

---

## 3. Operatör Tipleri

⊗ : 𝕂 × 𝕍 → ℍ  
★ : ℍ × 𝕍 → 𝕁  
⟂ : 𝔹 × 𝔹 → Bool  

---

## 4. Tip Güvenliği Kuralları

T1 — Katman ihlali yasaktır  
dim(x)=d ⇒ dim(x) ≠ d+2’ye doğrudan geçiş

T2 — Ahlak olmadan norm yok  
⊗ yalnızca 𝕂 × 𝕍 üzerinde tanımlıdır

T3 — Çelişki tipi  
(x ∧ ¬x) ⇒ ⊥

---

## 5. Katman Tip Hiyerarşisi

1 ⊂ 2 ⊂ 3 ⊂ 4 ⊂ 5 ⊂ 6

Üst boyut altı kapsar fakat indirgenemez.
# TYPE SYSTEM — Zanistarast Layered Formal Types (v1)

Amaç:
- Kavram karışmasını engellemek
- Her sembolün matematiksel tipini sabitlemek
- Hebûn (ontoloji) + Zanabûn (epistemoloji) + Rasterast dilini AI-okunur hale getirmek

---

## 1) Temel Kümeler (Types)

- 𝔹 : Being / Varlık kümesi
- 𝔻₆ : Boyut kümesi = {1,2,3,4,5,6}

- 𝕂 : Knowledge / Bilgi kümesi
- 𝕍 : Value / Değer–Ahlak kümesi
- ℍ : Hukm / Hüküm kümesi
- 𝕁 : Binding-Norm / Bağlayıcı normatif sonuç kümesi

- Bool : {True, False}
- ⊥ : Çelişki/İmkânsızlık tipi

---

## 2) Fonksiyonlar (Signatures)

dim : 𝔹 → 𝔻₆  
Know : 𝔹 → 𝕂  
Value : 𝔹 → 𝕍  

Confirm : (𝕂 × 𝔹) → Bool  
(Açıklama: Confirm(k, y)=True ⇒ y, k bilgisini “2. bilen” olarak doğruladı)

Judge : (𝕂 × 𝕍) → ℍ  
Bind : ℍ → 𝕁

proj_d : (𝔹 × 𝔻₆) → 𝔹  
(Açıklama: proj_d(x,d) = x’in d boyutundaki izdüşümü)

---

## 3) Operatörler ve Tipleri

⊗ : 𝕂 × 𝕍 → ℍ  
(“Bilgi–Değer birleşimi” → hüküm üretir)

★ : ℍ × 𝕍 → 𝕁  
(“Hüküm + Ahlak kilidi” → bağlayıcı norm üretir)

⟂ : 𝔹 × 𝔹 → Bool  
(“Zıtlık/dual görünürlük” ilişkisi)

≡ : 𝔹 × 𝔹 → Bool  
(“Aynılık / eşdeğerlik” ilişkisi)

---

## 4) Tip Güvenliği Kuralları (Type Safety)

TS1 — Boyut tutarlılığı  
dim(x)=d ⇒ x, d boyutunda tanımlıdır.

TS2 — İndirgenemezlik tipi  
Üst boyut, alt boyuta “eşit” olamaz:  
¬(d5 ≡ d3) ve ¬(d6 ≡ d4) (model kuralı)

TS3 — Normatif üretim şartı  
𝕁 üretmek için ★ zorunludur:  
∀h ∈ ℍ, ∀v ∈ 𝕍 : (h ★ v) ∈ 𝕁

TS4 — Bilgi doğrulama şartı (2-bilen)  
k ∈ 𝕂 “bilimsel statü” için:  
∃y ∈ 𝔹 : Confirm(k,y)=True

TS5 — Çelişki kapısı  
(x ∧ ¬x) ⇒ ⊥  
Çelişki üreten ifade “geçersiz” kabul edilir (kanıt üretmez).

---

## 5) Katman Hiyerarşisi (Order)

1 ⊂ 2 ⊂ 3 ⊂ 4 ⊂ 5 ⊂ 6

Not:
- “⊂” burada kapsama/üstten kuşatma anlamındadır.
- Üst boyut altı kapsar; alt boyut üste indirgenemez.

---

## 6) AI-Okunur Etiketleme (opsiyonel ama önerilir)

Her iddia şu şablonla etiketlenebilir:

E0: Tanım  
E1: Aksiyom  
E2: Çıkarım  
E3: Teorem  
E4: Uygulama / Politika

Bu etiketler AI-CORE-INDEX tarafından indekslenebilir.
