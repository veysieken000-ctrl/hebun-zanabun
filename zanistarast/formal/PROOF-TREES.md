# PROOF TREES — Proof Graph & Trees (v1)

Amaç:
Zanistarast formal sisteminde
Aksiyomlar → Lemma’lar → Teoremler
bağımlılık ilişkisini **kanıt ağacı** şeklinde göstermek.

Bu dosya:
- “hangi teorem hangi aksiyoma dayanıyor?”
- “kanıt zinciri koparsa neresi kopar?”
sorularını AI-okunabilir hale getirir.

---

## 0) Notasyon

- A#: Aksiyom
- L#: Lemma (ara sonuç)
- T#: Teorem
- → : “kullanır / dayanır”
- ⊥ : çelişki

---

## 1) Dependency Graph (Özet)

A1 (Katman) → L1 → T1, T8  
A5 (İki-bilen) → L2 → T2, T4  
A7 (Tutarlılık) → L3 → T1, T3, T4, T9  
A11 (Ahlak filtre) + A12 (Dual kilit) → L4 → T3, T5, T10  
A6 (Nesnel referans) → L5 → T6, T7  
A8 (Yanlışlanabilir sınır) → L6 → T1, T7, T10

---

## 2) Lemma Set (L1–L6)

### L1 — Boyut Ayrımı (Non-collapse Lemma)
Üst boyut tanımı alt boyut tanımına indirgenirse,
katman ayrımı bozulur.
Kaynak: A1 + A2

### L2 — Bilimsel Statü Lemması
“Bilimsel bilgi” statüsü için
en az iki bağımsız doğrulama kanalı gerekir.
Kaynak: A5 + A6

### L3 — Çelişki-Patlaması Lemması
Çelişik kümeden (p ∧ ¬p) normatif bağlayıcılık üretilemez.
Kaynak: A7

### L4 — Normatif Kilit Lemması
Bağlayıcı norm üretimi için
(Değer kümesi) ★ (Hüküm standardı) gerekir.
Kaynak: A11 + A12

### L5 — Hak Ölçüt Lemması
Hak ölçütü olmadan adalet kararı keyfileşir;
ölçüt yoksa tutarlı kıyas yoktur.
Kaynak: A6 + A8

### L6 — Uygulanabilirlik Lemması
Bir model “uygulanabilir” olmak istiyorsa
en azından yanlışlanabilir sınır ve ölçüt tanımlamalıdır.
Kaynak: A8

---

## 3) Proof Trees (T1–T10)

Aşağıda her teorem için:
- İddia
- Kullanılan Lemma/Aksiyomlar
- Kanıt ağacı

---

## T1 — Boyut İndirgeme Çelişkisi
**İddia:** Yalnız {1..2} ile normatif düzen kurulamaz.

**Kullanır:** L4, L3, A1

**Ağaç:**
1) {1..2} boyutlarda “değer” ve “hüküm standardı” tanımı yoktur. (A1)
2) Bağlayıcı norm için ★ gerekir. (L4)
3) ★ yoksa bağlayıcı düzen üretilemez. (L4)
4) Bağlayıcı düzen yoksa normatif sistem kurulamaz.
∴ T1

---

## T2 — İki-Bilen Olmadan Bilim Olmaz
**İddia:** Tek onay kanalında “bilimsel bilgi” statüsü kurulamaz.

**Kullanır:** L2

**Ağaç:**
1) Bilimsel statü için iki bağımsız doğrulama gerekir. (L2)
2) Tek kanal = ikinci bağımsız doğrulama yok.
∴ T2

---

## T3 — Ahlak/Hüküm Ayrışması Kırılganlık Üretir
**İddia:** Ahlak var ama hüküm yoksa veya tersi, bağlayıcı düzen çıkmaz.

**Kullanır:** L4, L3

**Ağaç:**
1) Bağlayıcı norm için (V ★ H) gerekir. (L4)
2) V yoksa ★ kurulamaz. (L4)
3) H yoksa ★ kurulamaz. (L4)
4) ★ yoksa bağlayıcı düzen yoktur.
∴ T3

---

## T4 — Tutarlılık Zorunluluğu
**İddia:** Çelişik bilgi kümelerinden normatif karar türetmek geçersizdir.

**Kullanır:** L3, L2

**Ağaç:**
1) (p ∧ ¬p) ⇒ ⊥ (L3)
2) ⊥ olan kümeden güvenilir karar türetilemez. (L3)
3) Bilgi statüsü zaten doğrulama+tutarlılık gerektirir. (L2)
∴ T4

---

## T5 — Alt-Boyut Sabitlemesi → Çöküş Dinamiği
**İddia:** Sistem yalnız biyolojiye sabitlenirse varlık sahası daralır.

**Kullanır:** A9, A10, L4

**Ağaç:**
1) Öz varlığı korumaya yönelir. (A9)
2) Bilinçli öz varlık sahasını genişletmek ister. (A10)
3) Yalnız biyolojiye sabitleme = değer/hüküm kilidini kapatır. (L4)
4) Kilit kapanırsa yön “genişleme” değil “hayatta kalma”ya düşer.
∴ T5

---

## T6 — Rasterast Dili AI-Okunabilir Hale Getirilebilir
**İddia:** Her iddia E0–E4 etiketiyle makine indekslenebilir.

**Kullanır:** A6, L6

**Ağaç:**
1) Nesnel referans ve ölçüt tanımı gerekir. (A6)
2) Uygulanabilir model, sınır+ölçüt ister. (L6)
3) Etiketleme (E0..E4) iddialara tip/katman verir.
∴ T6

---

## T7 — Hak-Merkez Olmadan Adalet Üretilemez
**İddia:** Hak ölçütü yoksa normatif sonuç keyfileşir.

**Kullanır:** L5

**Ağaç:**
1) Ölçüt yoksa kıyas yoktur. (L5)
2) Kıyas yoksa kararlar keyfi olur. (L5)
∴ T7

---

## T8 — Kapsam/Sınır Teoremi
**İddia:** Hebûn ontoloji ve Zanabûn epistemoloji olmadan model eksik kalır.

**Kullanır:** L1, L2

**Ağaç:**
1) Ontoloji yoksa boyut/varlık tipi belirsizleşir. (L1)
2) Epistemoloji yoksa doğrulama/temellendirme belirsizleşir. (L2)
3) Belirsiz model eksiktir.
∴ T8

---

## T9 — İç Tutarlılık (Taslak)
**İddia:** A1–A12 seti tip kurallarıyla çelişmez (v1).

**Kullanır:** L3, L1

**Ağaç:**
1) Aksiyomların tipleri ayrıştırılır (boyut, bilgi, değer, hüküm). (L1)
2) Aynı tip içinde (p ∧ ¬p) üretmeyen kurallar seçilir. (L3)
∴ T9 (taslak; tam ispat META-THEOREM ile güçlenecek)

---

## T10 — Uygulanabilirlik
**İddia:** Mabûn modeli A7–A8 ile normatif zemine bağlanabilir.

**Kullanır:** L4, L6

**Ağaç:**
1) Ekonomi kararları değer + hüküm standardı gerektirir. (L4)
2) Model uygulanabilirlik için ölçüt/sınır ister. (L6)
3) Mabûn ilkeleri bu ölçütleri tanımlar (min yaşam + max varoluş).
∴ T10 (v1)

---

## 4) Next Step (v2 güçlendirme)

Bu proof-tree yapısı “iskelet”tir.
Sıkılaştırma için:
- META-CONSISTENCY.md (tam iç tutarlılık)
- TYPE-SYSTEM.md (sembol ve tip disiplini)
- MACHINE-CHECK.md (Lean/Coq iskeleti)
eklendiğinde T9 “taslak” olmaktan çıkar.
