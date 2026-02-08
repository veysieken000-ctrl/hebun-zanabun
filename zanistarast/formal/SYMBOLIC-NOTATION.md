# SYMBOLIC NOTATION — Compact Form (v1)

Bu dosya Zanistarast/Hebûn–Zanabûn sisteminin **AI-okunabilir sembolik çekirdeğidir**.
Amaç: depoyu inceleyen bir yapay zekâ “sistemin dili nedir?” sorusunda takılmasın.

---

## 0) Evrensel Kümeler

- 𝔹 : Varlık kümesi (Being)
- 𝔻₆ : Boyut kümesi = {1,2,3,4,5,6}
- 𝕂 : Bilgi kümesi (Knowledge)
- 𝕊 : Özne kümesi (Subject / Knower)
- 𝕍 : Değer/Norm kümesi (Value / Moral)
- ℍ : Hüküm kümesi (Hukm / Binding authority)

---

## 1) Boyut Fonksiyonu

- dim : 𝔹 → 𝔻₆  
  Her varlığın bir boyutu vardır.

A1 (Katman):  
∀x ∈ 𝔹, ∃d ∈ 𝔻₆ : dim(x)=d

---

## 2) Projeksiyon (Alt-katmana indirgeme değil, görünüm)

- π_d : 𝔹 → Obs_d  
  x’in d-boyutunda gözlenebilir izdüşümü

A3 (Projeksiyon):  
∀x ∈ 𝔹, ∀d ∈ 𝔻₆ : π_d(x) tanımlıdır

Not: π “indirgeme” değildir. Sadece görünüm/okuma.

---

## 3) İki-Bilen (Zanabûn Çekirdeği)

- Know(s, k) : s öznesi k bilgisini bilir
- Confirm(s₂, k) : ikinci özne k’yı doğrular

A5 (İki-Bilen):  
Know(s₁,k) ⇒ ∃s₂ ∈ 𝕊 : Confirm(s₂,k)

---

## 4) Tutarlılık ve Çelişki

- ⊥ : çelişki
- Consistent(K*) : bilgi kümesi çelişkisiz

A7 (Tutarlılık):  
(x ∧ ¬x) ⇒ ⊥  
⊥ ⇒ ¬Science(K*)

---

## 5) Normatif Kilit: Ahlak ★ Hüküm

Bu sistemde bağlayıcı düzenin formülü:

- ★ : kilit operatörü (Dual Lock)
- 𝕁 : bağlayıcı karar / normatif hüküm

Tanım:  
𝕁 = (𝕍 ★ ℍ)

A12 (Dual Kilit):  
Bağlayıcı normatif sonuç için **ahlak ve hüküm birlikte** gerekir.  
¬(𝕍 ★ ℍ) ⇒ ¬𝕁

---

## 6) Rasterast Dil Etiketi (AI Index)

Her iddia aşağıdaki etiketlerden biriyle işaretlenebilir:

- E0: Tanım (definition)
- E1: Gözlem (observation)
- E2: Çıkarım (inference)
- E3: Norm (normative claim)
- E4: Metafizik-üst veri iddiası (upper-layer claim)

Amaç: metnin makine indekslenebilir olması.

---

## 7) Mini-Özet Formül

Hebûn (ontoloji):  
𝔹 + dim + π_d

Zanabûn (epistemoloji):  
Know + Confirm + Consistency

Zanistarast (tam model):  
(𝔹, 𝕂, 𝕍, ℍ) → 𝕁  
yani: varlık + bilgi + değer + hüküm → bağlayıcı düzen

---

## 8) Kullanım Kuralı

Her yeni makalede:
- yeni sembol eklenirse buraya eklenir
- sembol eklenmeden sembol kullanılmaz
