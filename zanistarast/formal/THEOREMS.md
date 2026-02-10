# THEOREMS — T1..T10 (v1)

T1 (Boyut indirgeme çelişkisi):
Yalnız {1..2} ile normatif düzen kurulamaz. (A7,A8)

T2 (İki-bilen olmadan bilim olmaz):
Tek onay kanalında “bilimsel bilgi” statüsü kurulamaz. (A4)

T3 (Ahlak-hüküm ayrışması sistem kırılganlığı üretir):
Ahlak var ama hüküm yoksa veya tersi, bağlayıcı düzen çıkmaz. (A7)

T4 (Tutarlılık zorunluluğu):
Çelişik bilgi kümelerinden normatif karar türetmek geçersizdir. (A5,A7)

T5 (Alt-boyut sabitlemesi → çöküş dinamiği):
Sistem sadece biyolojiye sabitlenirse varlık sahası daralır. (A11,A12)

T6 (Rasterast dili “AI-okunabilir” hale getirilebilir):
Her iddia E0–E4 etiketiyle makine indekslenebilir. (A6,A9,A10)

T7 (Hak-merkez olmadan adalet üretilemez):
Hak ölçütü yoksa normatif sonuç keyfileşir. (A8)

T8 (Kapsam/ sınır teoremi):
Hebûn ontoloji, Zanabûn epistemoloji olmadan “model” eksik kalır. (A1-A6)

T9 (İç tutarlılık):
A1-A12 seti kendi içinde tip kurallarıyla çelişmez (taslak).

T10 (Uygulanabilirlik):
Mabûn ekonomik model, A7-A8 ile normatif zemine bağlanabilir (taslak).
# THEOREMS — T1..T10 (v1)

Bu dosya aksiyomlardan türeyen ana teoremleri listeler.
Detaylı kanıtlar proofs/ klasöründedir.

---

## T1 — Boyut indirgeme çelişkisi
Yalnız {1..2} boyutla normatif düzen kurulamaz.
(A7, A11, A12)

---

## T2 — İki-bilen olmadan bilim olmaz
Tek doğrulama kanalı bilim statüsü oluşturamaz.
(A5)

---

## T3 — Ahlak-hüküm ayrışması kırılganlık üretir
Ahlak var ama hüküm yoksa bağlayıcılık oluşmaz.
(A12)

---

## T4 — Tutarlılık zorunluluğu
Çelişik kümelerden normatif karar üretilemez.
(A7)

---

## T5 — Alt-boyut sabitlemesi çöküş üretir
Sistem yalnız biyolojik düzeye sabitlenirse varlık sahası daralır.
(A9, A10)

---

## T6 — Rasterast iddiaları makine-indekslenebilir
Her iddia aksiyom referansıyla etiketlenebilir.
(A6)

---

## T7 — Hak-merkez olmadan adalet üretilemez
Referans yoksa normatif sonuç keyfileşir.
(A6, A11)

---

## T8 — Ontoloji + Epistemoloji birlikte gerekir
Hebûn olmadan Zanabûn eksiktir, Zanabûn olmadan model eksiktir.
(A1–A6)

---

## T9 — İç tutarlılık
A1–A12 kümesi tip sistemiyle çelişmez.
(taslak)

---

# META-THEOREM — Structural Consistency Lock (v1)

Amaç:
Aksiyomlar (A1–A12) + Çıkarım Kuralları (R1–R6) birlikte
sistemin iç tutarlılığını garanti eder mi?

Bu belge sistemi “kilitlemek” için yazılmıştır.

---

## META-T1 — Tutarlılık Korunumu

Eğer:

1) A1–A12 çelişkisiz ise
2) R1–R6 çelişki üretmeyen kurallarsa

O halde:

Sistem içsel olarak tutarlıdır.

---

## Kanıt Taslağı

1) Aksiyomlar temel doğrulardır.
2) R2 (Çelişki Eliminasyonu) gereği,
   (x ∧ ¬x) ⇒ ⊥
3) Çıkarım kuralları yalnızca
   mevcut aksiyomlardan türetim yapar.
4) Yeni bir çelişki üretmeyen türetim sistemi
   tutarlılığı korur.

Sonuç:
A1–A12 + R1–R6 birlikte
kapalı ve çelişkisiz bir yapı oluşturur.
### MT2 — 4→5 Zorunluluğu (Normatif Yansıma Kilidi)

Katman 4 (Kanun/Ruh + Uygulama) 
tek başına normatif anlam üretmez.

Bağlayıcı ahlaki düzen için
Katman 5 (Ahlak/Normatif Bilinç) zorunludur.

Proof: formal/proofs/MT2.md

Used Axioms:
A2, A7, A9, A10, A11, A12
---

## META-T2 — Katman Kilidi

Hiçbir teorem:

D5 ve D6 olmadan normatif sonuç üretemez.

Kanıt:

1) R3 gereği ★(D5,D6) ⇒ 𝕁
2) D5 veya D6 yoksa ★ tanımsızdır.
3) Tanımsız yapıdan 𝕁 üretilemez.

Bu nedenle:

Alt-boyut indirgemesiyle
normatif bilim kurulamaz.

---

## META-T3 — Genişleme Uyumluluğu

Yeni aksiyom eklenebilir,
ancak:

• Tip sistemini ihlal etmemeli
• Çelişki üretmemeli
• Katman hiyerarşisini bozmamalıdır

Aksi halde sistem revize edilmelidir.

---
---

### MT4 — Full Stack Necessity (1–6 Inseparability)

Katmanlar 1–6 ayrıştırılamaz.
Her katman varlık düzeninin zorunlu bileşenidir.

Herhangi bir katmanın çıkarılması
sistem çöküşüne yol açar.

Proof: formal/proofs/MT4.md

Used Axioms:
A1, A2, A7, A11, A12

---

### MT5 — Aşkın Temel Gereklilik (6+Ehad)

Katman 6 (Son Karar) kendi kendine topraklanamaz.

Herhangi bir kapalı 1-6 sistemi gerektirir
Sınırlı olmayan bir topraklama ilkesi.

Bu temellendirmeyi 𝔈 (Ehad) olarak gösterelim.

Kanıt: formal/proofs/MT5.md

Kullanılan Aksiyomlar:
A1, A2, A7, A12
## T10 — Uygulanabilirlik
Mabûn modeli aksiyom setiyle normatif zemine bağlanabilir.

# META-THEOREM — Structural Consistency Lock (v1)

Amaç:
Aksiyomlar (A1–A12) + Çıkarım Kuralları (R1–R6) birlikte
sistemin iç tutarlılığını garanti eder mi?

Bu belge sistemi “kilitlemek” için yazılmıştır.

---

## META-T1 — Tutarlılık Korunumu

Eğer:

1) A1–A12 çelişkisiz ise
2) R1–R6 çelişki üretmeyen kurallarsa

O halde:

Sistem içsel olarak tutarlıdır.

---

## Kanıt Taslağı

1) Aksiyomlar temel doğrulardır.
2) R2 (Çelişki Eliminasyonu) gereği,
   (x ∧ ¬x) ⇒ ⊥
3) Çıkarım kuralları yalnızca
   mevcut aksiyomlardan türetim yapar.
4) Yeni bir çelişki üretmeyen türetim sistemi
   tutarlılığı korur.

Sonuç:
A1–A12 + R1–R6 birlikte
kapalı ve çelişkisiz bir yapı oluşturur.

---

## META-T2 — Katman Kilidi

Hiçbir teorem:

D5 ve D6 olmadan normatif sonuç üretemez.

Kanıt:

1) R3 gereği ★(D5,D6) ⇒ 𝕁
2) D5 veya D6 yoksa ★ tanımsızdır.
3) Tanımsız yapıdan 𝕁 üretilemez.

Bu nedenle:

Alt-boyut indirgemesiyle
normatif bilim kurulamaz.

---

## META-T3 — Genişleme Uyumluluğu

Yeni aksiyom eklenebilir,
ancak:

• Tip sistemini ihlal etmemeli
• Çelişki üretmemeli
• Katman hiyerarşisini bozmamalıdır

Aksi halde sistem revize edilmelidir.

---
# META-THEOREM — Internal Consistency Lock (v1)

Bu dosya, Zanistarast aksiyom setinin (A1–A12) “kilit” seviyesindeki
iç tutarlılık çerçevesini ve meta-teoremini tanımlar.

Amaç:
- Sistemin “her şey her şeye gider” tipinde gevşek yorumlanmasını engellemek
- Aksiyomları tip sistemi + çıkarım kuralları ile sınırlandırmak
- Teorem üretimini kontrollü hale getirmek

---

## 0) Notasyon ve Tipler (Minimal)

Boyut kümesi:
- 𝔻 = {1,2,3,4,5,6}

Varlık kümesi:
- 𝔹 = “varlık taşıyıcıları” (being instances)

Bilgi kümesi:
- 𝕂 = doğrulanabilir bilgi nesneleri

Normatif bağlayıcılık (hukuki/ahlaki bağ):
- 𝕁 = bağlayıcı hüküm/karar çıktısı

Özel operatör:
- ★ = “Dual Kilit Operatörü” (Ahlak × Hüküm birlikte)

Kural:
- ★ uygulanmadan 𝕁 türetilemez.

---

## 1) Çıkarım Kuralları (Minimal Proof Discipline)

R1 — Non-contradiction gate  
Eğer Γ ⊢ (p ∧ ¬p) ise Γ çökmüş kabul edilir ve normatif çıktı (𝕁) üretilemez.

R2 — Typing gate  
Her ifade bir tipe sahip olmalıdır:
- varlık ifadesi → 𝔹
- bilgi ifadesi → 𝕂
- normatif sonuç → 𝕁

Tipi belirsiz ifade “kanıt adımı” sayılamaz.

R3 — Dimension discipline  
Bir iddia dim(d) belirtmeden “boyut iddiası” olamaz.
Örn: “indirgenemezlik” iddiası boyutları açıkça söylemek zorundadır.

R4 — Dual Lock discipline  
Normatif sonuç çıkarımı için:
- Ahlak bileşeni + Hüküm bileşeni birlikte sağlanmadan
- 𝕁 türetilemez.

---

## 2) META-THEOREM (MT1) — “Kilit Tutarlılık” Teoremi

**MT1 (Kilit Tutarlılık):**  
(A1–A12) aksiyom seti, R1–R4 disiplin kuralları altında
normatif sonuç üretirken çelişkiye düşmeden çalışacak şekilde kısıtlanabilir.

Formel ifade:
Eğer
- Γ = {A1..A12}
- çıkarım kuralları = {R1..R4}
ise

> Γ ⊬ ⊥ (yani “doğrudan çelişki” türetilemez)
ve
> Γ ⊢ 𝕁 yalnızca ★ kapısından geçerek türetilebilir.

---

## 3) MT1 Kanıt Fikri (Proof Sketch)

1) R2 tip kapısı sayesinde “ne olduğu belli olmayan semboller” ile çelişki üretilemez.  
   (Çünkü tip yoksa adım yoktur.)

2) R1 çelişki kapısı, bir yerde çelişki üretilirse sistemin normatif üretimi durur.  
   Bu sayede çelişki üzerinden keyfi sonuç türetme engellenir.

3) R3 boyut disiplini, “5’i 3’e indirgerim” gibi belirsiz indirgeme oyunlarını engeller.

4) R4 (★) disiplini, Ahlak veya Hüküm tek başına varken
   “bağlayıcı düzen” iddiası kurulmasını engeller.

Sonuç:
- Sistem “açık uçlu metafizik” değil,
- kontrollü çıkarım üreten bir aksiyomatik çerçevedir.

---

## 4) Teorem Kataloğuna Bağ

Bu meta-teorem, THEOREMS.md’deki özellikle şu teoremleri “kilitler”:
- T1 (alt boyuta indirgeme → normatif çöküş)
- T3 (ahlak/hüküm ayrışması → kırılganlık)
- T9 (iç tutarlılık iddiası)

Bu dosya, T9’un “kanıt standardı”dır.

---

## 5) Sistem Kilidi (Pratik Kural)

Zanistarast’ta şu kural “kilit”tir:

> Her normatif iddia (adalet, hukuk, hüküm) ★ kapısından geçmek zorundadır.

★ yoksa:
- iddia “yorum” olabilir
- ama “bağlayıcı bilimsel norm” olamaz

---

Durum: MT1 eklendi → sistemin iç tutarlılığı için savunma katmanı aktif.

# Proof — T11 (v1)

## İddia
Sistem kendi içinden mutlak doğrulama üretemez.

## Kullanılan aksiyomlar
A6, A7, A13

## Kanıt taslağı
1) S = (x,y) ikili yapı olsun.
2) S içindeki her doğrulama mekanizması S’nin parçasıdır.
3) Doğrulayıcı da doğrulanacak şeye bağımlı hale gelirse döngü oluşur.
4) Döngü, tutarlılık üretmez (A7).
5) Döngüyü kırmak için sistem dışı referans gerekir (A6).
6) Sistem dışı referans, üst-perspektiftir (A13).
Sonuç: Mutlak doğrulama iç sistemden çıkmaz. QED.

# THEOREMS — T1..T10 (v1)

Her teorem ilgili proof dosyasına bağlanmıştır.

---

## T1 — Boyut indirgeme çelişkisi
Yalnız {1..2} ile normatif düzen kurulamaz.  
(A7, A8)  
Proof: proofs/T1.md

---

## T2 — İki-bilen olmadan bilim olmaz
Tek onay kanalında “bilimsel bilgi” statüsü kurulamaz.  
(A5, A6, A7)  
Proof: proofs/T2.md

---

## T3 — Ahlak–Hüküm ayrışması sistem kırılganlığı üretir
Ahlak var ama hüküm yoksa veya tersi, bağlayıcı düzen çıkmaz.  
(A12, A7)  
Proof: proofs/T3.md

---

## T4 — Tutarlılık zorunluluğu
Çelişik bilgi kümelerinden normatif karar türetmek geçersizdir.  
(A7, A5, A8)  
Proof: proofs/T4.md

---

## T5 — Alt-boyut sabitlemesi → çöküş dinamiği
Sistem sadece biyolojiye sabitlenirse varlık sahası daralır.  
(A9, A10, A11)  
Proof: proofs/T5.md

---

## T6 — Rasterast dili AI-okunabilir hale getirilebilir
Her iddia E0–E4 etiketiyle makine indekslenebilir.  
(A6, A5, A7)  
Proof: proofs/T6.md

---

## T7 — Hak-merkez olmadan adalet üretilemez
Hak ölçütü yoksa normatif sonuç keyfileşir.  
(A8, A7, A12)  
Proof: proofs/T7.md

---

## T8 — Kapsam / Sınır Teoremi
Hebûn ontoloji ve Zanabûn epistemoloji olmadan model eksik kalır.  
(A1–A6)  
Proof: proofs/T8.md

---

## T9 — İç Tutarlılık
A1–A12 seti tip kurallarıyla çelişmez (taslak).  
(TYPE-SYSTEM referansı)  
Proof: proofs/T9.md

---

## T10 — Uygulanabilirlik
Mabûn ekonomik model, A7–A8 ile normatif zemine bağlanabilir.  
(A7, A8, A12)  
Proof: proofs/T10.md

---

### MT6 — System Completeness Theorem

The 6-layer structure (1–6),
together with transcendental ground 𝔈,
forms a dimensionally closed,
internally consistent,
non-reducible ontological system.

No additional structural layer is required.

Proof: formal/proofs/MT6.md

Used Axioms:
A1–A12
MT1–MT5
