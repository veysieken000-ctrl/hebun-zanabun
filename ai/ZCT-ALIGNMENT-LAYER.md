# ZCT Hizalama Katmanı – Üst Ölçü Dikkat Modeli

## Soyut

Bu belge, ZCT'nin (Zanistarast Çekirdek Teorisi) hizalama katmanını tanımlar.

Hizalama, bir üst ölçü fonksiyonu H'ye uygulanan bir dikkat parametresi λ olarak modellenmiştir.

Karar kuralı:

Skor_λ(s,u) = λH(s,u) + E(s,u)

Nerede:

- H(s,u): Üst değer hizalama fonksiyonu
- E(s,u): Çevresel/sistem uyumluluğu
- λ ∈ [0,1]: Üst ölçü dikkat parametresi

Sürüklenme şu şekilde tanımlanır:

Sürüklenme = 1 − λ

Hizalama hatası λ → 0 olduğunda meydana gelir.

---

## 1. Temel Fikir

Hizalama ikili bir işlem değildir.

Bu süreklidir ve λ tarafından yönetilir.

Yüksek λ:
- Yüksek değerler kararları büyük ölçüde etkiler.

Düşük λ:
- Kısa vadeli veya sistem düzeyinde optimizasyon baskındır.

---

## 2. Sürüklenme

Kayma, üst değer ihmalini ölçer.

Sürüklenme = 1 − λ

Sürüklenme arttıkça:
- Normatif ihmal artar
- Değer uyumsuzluğu riski artar

---

## 3. Yapay Zeka Yorumlaması

İnsan modeli:
- O (öz)
- M (ahlaki alan)
- λ (üst ölçüye dikkat)

Yapay zeka modeli:
- H = hizalama hedefi
- λ = değer dikkat ağırlığı
- Sapma = hizalama hatası riski

---

## 4. Katkı

Bu çerçeve:

- Hizalamayı ölçülebilir hale getirir
- Değer odaklılığı kontrol etmek için bir kontrol parametresi sunar.
- Etik sapmayı dikkat dinamikleriyle ilişkilendirir.

---

## 5. Gelecekteki Genişletmeler

- Dinamik λ(t)
- Stabilite analizi
- Çoklu ajan hizalama kayması
