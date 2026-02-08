# TYPES — Entities, Statements, Evidence (v1)

## 1) Temel Tipler
- Being (𝔹): insan, toplum, kurum, canlı, fiziksel nesne (soyut/ somut)
- Knowledge (𝕂): önerme, model, veri, gözlem, yorum
- Value (𝕍): adalet, vicdan, hak, iyilik/doğruluk kısıtları
- Judgment (𝕁): hükme bağlanmış sonuç (bağlayıcı çıktı)

## 2) Önerme Tipleri
- Descriptive φ: “olan”
- Normative ψ: “olması gereken”
- Meta χ: “bilginin şartı / yöntemi”

## 3) Delil Seviyeleri (AI için)
- E0: tanım
- E1: gözlem/tekrar
- E2: model uyumu (tutarlılık)
- E3: falsifiye edilebilirlik sınırı
- E4: değer-norm uyumu (ahlak/hüküm kilidi)
4) Aksiyom seti (A1, A2, …) — “sarsılmaz omurga”

# TYPES — Type System (v1)

Amaç:
Her nesnenin tipi bellidir.
AI "x nedir?" diyemez.

---

## 1. Temel Tipler

Being (𝔹)  
→ İnsan, toplum, canlı, fizik nesnesi

Knowledge (𝕂)  
→ Veri, önerme, model

Value (𝕍)  
→ Hak, adalet, vicdan ölçütleri

Judgment (𝕁)  
→ Bağlayıcı normatif sonuç

---

## 2. Önerme Tipleri

Descriptive φ  
→ Olan

Normative ψ  
→ Olması gereken

Meta χ  
→ Yöntemsel / bilgi-şartı

---

## 3. Delil Seviyesi

E0 → Tanım  
E1 → Gözlem  
E2 → Tutarlılık  
E3 → Falsifiye sınırı  
E4 → Ahlak-hüküm kilidi

---

## 4. Tip Kuralı

- Aynı tip ⊕ ile birleşir.
- Farklı tip ⊗ ile etkileşir.
- Normatif sonuç için (𝕂 ⊗ 𝕍) gerekir.

# TYPES — Formal Type System (v1)

Amaç:
- Sembolleri “ne tür şeyler” olduklarıyla sabitlemek
- Çelişkiyi tip seviyesinde engellemek
- Aksiyom/teorem üretimini AI-okunabilir hale getirmek

---

## 0) Tip Evrenleri

- 𝔹 : Varlıklar kümesi (Being-domain)
- 𝔻₆ : Boyutlar kümesi = {1,2,3,4,5,6}
- 𝕂 : Bilgi nesneleri (Knowledge-objects)
- 𝕍 : Değer / normatif işaretler (Value-tags)
- 𝕁 : Bağlayıcı hüküm çıktıları (Judgement-outputs)
- 𝔸 : Aksiyomlar
- 𝕋 : Teoremler

---

## 1) Temel Fonksiyonlar (Tip İmzaları)

- dim : 𝔹 → 𝔻₆
- proj_d : 𝔹 → 𝔹 (d ∈ 𝔻₆ için tanımlı projeksiyon)
- Know : 𝕂 → Bool
- Confirm_y : 𝕂 → Bool (y bir bilen/ajan; ajanları ayrıca tanımlarız)
- Consistent : ℘(𝕂) → Bool
- ★ : (𝕍 × 𝕁) → 𝕁 (Ahlak–Hüküm kilidi operatörü: bağlayıcı hüküm üretir)

Not:
★ bir “aritmetik çarpım” değildir.
★ bir “normatif bağlayıcılık operatörü”dür.
Tipi: (değer, hüküm) -> bağlayıcı hüküm.

---

## 2) Boyut Tipleri (Sadece sınıflandırma)

- D1: Fizik
- D2: Biyoloji
- D3: Zihin
- D4: Kanun/Ruh (doğa-düzeni)
- D5: Ahlak (normatif niyet/erdem katmanı)
- D6: Hüküm (nihai bağlayıcılık / sonuç katmanı)

Boyutlar “alt-kümeye indirgenemez”.
Bu ifade set-teorik değil; tip-teorik bir kısıttır:
D5 ≠ D3, D6 ≠ D4 ve D5,D6 tipleri farklıdır.

---

## 3) Yasaklı Tip Hataları (Çelişkiyi kıran şeyler)

T-Hata-1:
dim(x)=5 iken x’i “salt D3 nesnesi” gibi kullanmak.

T-Hata-2:
★ operatörünü (𝕂×𝕂)->𝕂 gibi kullanmak.

T-Hata-3:
Confirm fonksiyonunu “tek ajan”a kilitleyip evrenselleştirmek
(“iki-bilen” koşulu bozulur).

---

## 4) Minimum Tip Disiplini Kuralı

Her teorem/proof şu şablonu taşımalı:

- Kullanılan semboller
- Her sembolün tipi
- Kullanılan çıkarım kuralı (INFERENCE-RULES.md’den)
- Sonucun tip
