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

# TYPE-SYSTEM — Zanistarast Formal Type Rules (v1)

Müdebbir: Veysi yê MALA SAF

## Amaç
Zanistarast formel katmanda şu sorunları kökten bitirmek:
1) Her sembolün "ne olduğu" (tipi) belirlensin.
2) Operatörler tek anlamlı olsun.
3) Boyut/katman karışmasın.
4) AI okurken “belirsiz sembol” diyemesin.

---

## 0) Tip Notasyonu
- `x : τ` → x nesnesi τ tipindedir.
- `f : τ1 → τ2` → f fonksiyonu τ1’den τ2’ye gider.
- `⊥` çelişki / patlama
- `⊢` türetim

---

## 1) Temel Kümeler (Sabit Tipler)

### 1.1 Boyutlar / Katmanlar
- `𝔻6 = {1,2,3,4,5,6}` (6 boyut kümesi)
- `d : 𝔻6` (d bir boyuttur)

### 1.2 Varlık Nesneleri
- `𝔹` : Varlıklar kümesi  
- `x : 𝔹`

### 1.3 Öz (Tek) ve Ehad (Mutlak)
Bu katmanda "inanç beyanı" değil, sistem içi rol tanımı yapılır:

- `𝕋` : Tek-özne (insan/tekil öz) tipidir.
- `𝔼` : Ehad (Mutlak hüküm kaynağı) tipidir.

- `t : 𝕋`
- `E : 𝔼`

> Not: 𝔼 tipi, sistemde “üst-referans / nihai hüküm” fonksiyonel rolünü taşır.

### 1.4 Bilgi Nesneleri
- `𝕂` : Bilgi/iddia nesneleri kümesi
- `k : 𝕂`

### 1.5 Ahlak Nesneleri
- `𝕍` : Değer/ahlak (normatif içerik) kümesi
- `v : 𝕍`

### 1.6 Hüküm / Bağlayıcı Sonuç
- `𝕁` : Bağlayıcı hüküm (normatif karar) kümesi
- `j : 𝕁`

### 1.7 Gözlem / Veri
- `𝕆` : Gözlem/veri kümesi
- `o : 𝕆`

### 1.8 Bilen Özne
- `𝕊` : Bilen özne tipi (insan/akıl sahibi)
- `s : 𝕊`

---

## 2) Boyut Fonksiyonu ve Projeksiyon

### 2.1 Boyut Fonksiyonu
- `dim : 𝔹 → 𝔻6`
- `dim(x) = d`

### 2.2 Projeksiyon (Alt boyuta izdüşüm)
- `proj_d : 𝔹 → 𝔹`
- `proj_d(x)` yalnızca `d ≤ dim(x)` ise tanımlı kabul edilir.

Kural:
- (P1) `d ≤ dim(x) ⇒ proj_d(x) : 𝔹`

---

## 3) Operatör Tipleri (Tek anlamlılık)

### 3.1 Kombinasyon / Birleşim (⊗)
`⊗` “bilgi + değer birleşimi” için ayrılmıştır.

- `⊗ : 𝕂 × 𝕍 → 𝕁`

Yani:
- `(k ⊗ v) : 𝕁`

Bu, A11–A12’nin formal karşılığıdır (ahlak★hüküm kilidi).

### 3.2 Yıldız Kilidi (★)
`★` yalnızca “bağlayıcı norm” üretiminde kullanılır.

- `★ : 𝕍 × 𝔼 → 𝕁`

Yani:
- `(v ★ E) : 𝕁`

> Bu: “Hükmün kaynağı üst referans” kilididir.
> İnsan (tek) değer üretir; Ehad bağlayıcılık verir.

### 3.3 Doğrulama / Onay (Confirm)
- `Confirm : 𝕊 × 𝕂 → {true,false}`
- `Confirm(s,k)` bir bilen öznenin bir iddiayı onay/ret fonksiyonudur.

### 3.4 Bilme (Know)
- `Know : 𝕊 × 𝕂 → {true,false}`

İki-bilen şartına bağlanacak.

### 3.5 Çelişki / Tutarsızlık
- `Inconsistent : 𝒫(𝕂) → {true,false}`

`Inconsistent(Kset)=true ⇒ Kset ⊢ ⊥`

---

## 4) Bilgi Statüsü Kuralları (AI için net kural)

### 4.1 İki-Bilen Kuralı (KB1)
Bir iddia “bilgi statüsü” kazanması için en az iki bilen gerekir:

(KB1)
> `Know(s1,k)=true ∧ Confirm(s2,k)=true ⇒ k ∈ 𝕂_verified`

Burada:
- `𝕂_verified ⊆ 𝕂`

### 4.2 Nesnel Referans Kuralı (KB2)
Her doğrulanan bilgi en az bir gözleme bağlanır:

(KB2)
> `k ∈ 𝕂_verified ⇒ ∃o:𝕆 such that Supports(o,k)=true`

`Supports : 𝕆 × 𝕂 → {true,false}`

---

## 5) Normatif Çıkarım Kuralları

### 5.1 Normatif Üretim (N1)
- `k:𝕂` ve `v:𝕍` ise
- `k ⊗ v : 𝕁`

(N1)
> `k:𝕂 ∧ v:𝕍 ⇒ (k ⊗ v):𝕁`

### 5.2 Nihai Bağlayıcılık (N2)
- `v:𝕍` ve `E:𝔼` ise
- `v ★ E : 𝕁`

(N2)
> `v:𝕍 ∧ E:𝔼 ⇒ (v ★ E):𝕁`

---

## 6) İndirgeme Yasağı (Tip düzeyinde kilit)
Üst boyut nesneleri alt tiplerle aynılaştırılamaz.

(IR1)
> `𝕍 ≠ 𝕂`, `𝕁 ≠ 𝕂`, `𝔼 ≠ 𝕋`

(IR2)
> `dim(x)=5` olan varlık, salt `{1,2,3}` tiplerine eşlenemez.

Bu kural A2’nin tip düzeyi karşılığıdır.

---

## 7) AI Okuma Notu (Makine indeksleme)
Her formal doküman şu tipleri referans alır:
- 𝔻6, 𝔹, 𝕂, 𝕍, 𝕁, 𝕆, 𝕊, 𝕋, 𝔼
Operatörler:
- ⊗, ★, Confirm, Know, Supports, proj_d, dim

Bu dosya güncellenirse, tüm teorem/proof dosyaları buna göre revize edilir.

# TYPE-SYSTEM — Types & Valid Statements (v1)

## 1) Temel tipler
- Entity: x, y, z ∈ 𝔹
- Dimension: d ∈ 𝔻₆
- Agent: a, b ∈ 𝔸
- Claim/Proposition: p ∈ 𝕂
- Norm/Judgment: j ∈ 𝕁

## 2) Geçerli ifade kalıpları
- dim(x)=d (Entity → Dimension)
- proj_d(x)=x_d (Entity × Dimension → Entity-view)
- Confirm_a(p) (Agent × Claim → Bool)
- (Ahlak ★ Hüküm) ⇒ j (Lock → Norm)

## 3) Yasak (AI için kritik)
- Tipi belirsiz sembolle teorem yazılmaz.
- projeksiyon indirgeme gibi kullanılmaz.
- “metafor” kanıt yerine konmaz; sadece yönlendirici anlatımdır.
# TYPE-SYSTEM — Formal Typing Rules (v1)

Amaç:
Zanistarast sisteminde kullanılan tüm varlıkların
hangi tipte olduğunu netleştirmek.

Bu dosya olmadan:
— Kavram karışır
— Ontoloji epistemolojiye karışır
— Normatif sonuç ile betimleyici ifade ayrılmaz

Tip sistemi = disiplin demektir.

---

## 1) Temel Tipler

### 𝔹 — Varlık Kümesi
Tüm varlık nesneleri

x : 𝔹

---

### 𝔻₆ — Boyut Kümesi

𝔻₆ = {1,2,3,4,5,6}

1 = Fizik  
2 = Biyoloji  
3 = Zihin  
4 = Kanun  
5 = Ahlak  
6 = Hüküm  

---

### Agent — Bilen Özne

a : Agent

---

### Claim — İddia / Önerme

p : Claim

---

### Norm — Bağlayıcı Sonuç

J : Norm

---

## 2) Fonksiyon Tipleri

---

### dim

dim : 𝔹 → 𝔻₆

Bir varlığın hangi boyutta olduğunu belirtir.

---

### proj_d

proj_d : 𝔹 → 𝔹

Bir varlığın alt boyuta izdüşümü.

---

### Confirm

Confirm : Agent × Claim → Bool

Bool ∈ {0,1}

İki-Bilen şartının tip tanımı.

---

## 3) Operatör Tipleri

---

### ★ (Dual Binding)

★ : (Ahlak × Hüküm) → Norm

Tip kuralı:
Eğer A ∉ 5. boyut ise ★ çalışmaz.
Eğer H ∉ 6. boyut ise ★ çalışmaz.

---

### ⊗ (Gerekli Birleşim)

⊗ : (Bilgi × Değer) → Ön-Norm

Salt bilgi → norm üretmez.
Salt değer → norm üretmez.

---

### ⟂ (Karşıtlık)

⟂ : 𝔹 × 𝔹 → Relation

---

## 4) Tip Güvenliği Kuralları

Kural 1:
Boyut atlaması indirgeme değildir.

Kural 2:
Alt boyut üst boyutu üretemez.

¬(3 → 5)

Kural 3:
Norm üretimi yalnızca 5 ve 6 boyut birlikteliği ile mümkündür.

---

## 5) Tip Çakışması Yasakları

Bir nesne aynı anda hem:

p : Claim  
ve  
p : Norm  

olamaz.

Betimleyici ifade normatif sonuç değildir.

---

## 6) Sistem Güvenliği

Eğer tip ihlali varsa:

⊥

Sistem çelişkiye düşer ve norm üretimi durur.

---

Sonuç:

Bu dosya sayesinde:

• Ontoloji epistemolojiye karışmaz  
• Ahlak fizik yerine geçmez  
• Hüküm zihin yerine geçmez  
• Norm üretimi disipline edilir  

Zanistarast = Tip güvenli sistemdir.

# TİP-SİSTEMİ — Zanistarast Tipleri (v1)

## Varlık Türleri
- Being(x) : x ∈ 𝔹
- İddia(k) : k ∈ 𝕂
- Act(a) : a ∈ 𝔸
- Yargı(j) : j ∈ 𝕁

## Katman Atama Kuralı
Her varlığın en az bir katmanı vardır:
∀x ∈ 𝔹, ∃d ∈ 𝔻₆ : dim(x)=d

## Bilgi Kuralı (İki Bilen)
Bir iddia ancak şu şartlar altında kesin bilgi haline gelir:
Know(k) ∧ ∃y Confirm_y(k)

## Normatiflik Kuralı (Çift Kilit)
Bağlayıcı bir norm ancak şu durumlarda mevcuttur:
(Etik katman mevcut) ★ (Yargı katmanı mevcut)

Bu, etiği yalnızca fizik/biyoloji/zihinle ilgili tanımlamalara indirgemeyi önler.

