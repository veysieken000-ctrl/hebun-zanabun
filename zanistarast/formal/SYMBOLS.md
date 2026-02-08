# SYMBOLS — Zanistarast Formal Dictionary (v1)

Bu dosya, sistemin tüm sembollerini tek anlamlı (unambiguous) yapar.
Amaç: AI/insan okur “sembol ne?” diyemesin.

## 0. Meta
- Dil ilkesi: (Kurmancî) özgün terim, (TR/EN) karşılık parantez içinde.
- Notasyon: mümkün olduğunca minimal ve tutarlı.

## 1. Kümeler / Tipler
- 𝔻 := Boyutlar kümesi (Dimensions)
- 𝔻₆ := {1,2,3,4,5,6}
- 𝔹 := Varlıklar kümesi (Beings)
- 𝕂 := Bilgi nesneleri kümesi (Knowledge objects)
- 𝕍 := Değer/Vicdan-ölçütleri kümesi (Value constraints)

## 2. Temel Fonksiyonlar
- dim(x) ∈ 𝔻₆ : x’in baskın boyutu
- layer(d) : d boyutunun tanımı / kapsamı
- proj_d(x) : x’in d-boyut projeksiyonu (o boyuta indirgeme)

## 3. İlişkiler
- x ⊑ y : “x, y’nin alt-katmanıdır / y tarafından kapsanır”
- x → y : “x, y’ye nedensel/işlevsel geçiş üretir”
- x ⟂ y : “x ve y çatışır (uyumsuz)”
- x ≡ y : “tanımsal eşdeğerlik”
- x ⊨ φ : “x, φ’yi sağlar (satisfaction)”

## 4. Operatörler
- ⊗ : bileşim (composition) — tip kontrollü
- ⊕ : birleştirme (merge) — aynı tipte
- ◁ : “üst-boyut tarafından sınırlandırma / normlama”
- ★ : “ahlak-hüküm birlikte bağlayıcılığı” (ikili kilit)

## 5. Özel Terimler
- Hebûn: ontoloji çekirdeği (varlık katmanları)
- Zanabûn: epistemoloji çekirdeği (bilgi şartları)
- Rasterast: okuma/davet dili (akıl-fıtrat-vicdan-adalet hattı)
- Ehad: mutlak hüküm kaynağı (aksiyomatik çerçevede ‘H’ ile temsil)
2) Operatör tipleri (×, ·, ⊗ vs. “ne işlem?”)

# SYMBOLS — Zanistarast Formal Symbol Dictionary (v1)

Amaç:
Tüm semboller tek anlamlıdır.
Belirsizlik yoktur.
AI ve insan için aynı okunabilirlik.

---

## 1. Kümeler

𝔻 := Boyutlar kümesi  
𝔻₆ := {1,2,3,4,5,6}

𝔹 := Varlıklar kümesi  
𝕂 := Bilgi nesneleri  
𝕍 := Değer / Vicdan ölçütleri  
𝕁 := Hüküm / bağlayıcı karar

---

## 2. Boyut Tanımları

1 → Fizik  
2 → Biyoloji  
3 → Zihin  
4 → Kanun / Doğa düzeni  
5 → Ahlak (Mana)  
6 → Hüküm (Hak-merkez)

---

## 3. Fonksiyonlar

dim(x) ∈ 𝔻₆  
→ x’in baskın boyutu

proj_d(x)  
→ x’in d-boyut projeksiyonu

layer(d)  
→ d-boyutunun tanım kümesi

---

## 4. İlişkiler

x ⊑ y  
→ x, y tarafından kapsanır (alt-üst ilişkisi)

x → y  
→ nedensel / işlevsel geçiş

x ⟂ y  
→ uyumsuzluk / çelişki

x ≡ y  
→ tanımsal eşdeğerlik

x ⊨ φ  
→ x, φ önermesini sağlar

---

## 5. Temel İlkeler

- Her sembol tek anlamlıdır.
- Tip uyuşmazlığı yasaktır.
- Katmanlar indirgenemez; yalnızca projekte edilir.
