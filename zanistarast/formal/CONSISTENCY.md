# CONSISTENCY — Internal Consistency Plan (v1)

Amaç:
A1–A12 aksiyom setinin ve çıkarım kurallarının
“iç çelişki üretmemesi”ni matematiksel olarak sıkılaştırmak.

Burada hedef:
- Tam “mutlak ispat” iddiası değil,
- Denetlenebilir bir “tutarlılık çerçevesi” (relative consistency).

---

## 1) Tutarlılık Tanımı

Sistem S = (A, R, T) olsun.

- A : aksiyomlar (AXIOMS.md)
- R : çıkarım kuralları (INFERENCE-RULES.md)
- T : tip sistemi (TYPES.md)

Tutarlılık:
S ⊬ ⊥
Yani: S’den çelişki (⊥) türetilemiyor olmalı.

---

## 2) En kritik kaynak: Tip Disiplini

Bu sistemde çelişkilerin %90’ı tip hatasından doğar.
Bu yüzden “Tip doğrulama” (R1) zorunludur.

Kural:
Tipi doğrulanmayan adım, sistemin parçası değildir.

---

## 3) Model-Şahit Yaklaşımı (Relative Consistency)

Bu sistem için bir “model şahit” veriyoruz:

- 𝔻₆ = {1,2,3,4,5,6} (sonlu küme)
- 𝔹 = herhangi bir boş olmayan küme
- dim : 𝔹 → 𝔻₆ (her elemanı bir boyuta atar)
- proj_d : 𝔹 → 𝔹 (her d için tanımlı bir fonksiyon)
- 𝕂, 𝕍, 𝕁 : boş olmayan üç küme
- ★ : (𝕍×𝕁)→𝕁 bir fonksiyon

Bu kurulumda:
- A1 “her varlık bir boyutta tanımlıdır” sağlanır.
- A7 “çelişki bilgi üretmez” R3 ile uyumludur.
- A12 “dual kilit” ★ operatörünün varlığıyla modellenir.

Sonuç:
Eğer temel küme kuramı (ZFC gibi) tutarlıysa,
bu yapı içinde S’nin ⊥ üretmesi engellenebilir.

Bu, “mutlak ispat” değil,
denetlenebilir “göreli tutarlılık” çerçevesidir.

---

## 4) Tutarlılığı bozan şeyler listesi (Kırmızı çizgiler)

C1) ★ operatörünü aritmetik gibi yorumlamak (tip ihlali)
C2) “Ahlak var ama hüküm yok” iken bağlayıcı hüküm iddia etmek (R5 ihlali)
C3) Tek doğrulama kanalını evrenselleştirmek (R7 ihlali)
C4) Üst-boyutu alt-boyuta “indirgeme” diye yazmak (A2 ile çelişir)

---

## 5) Tutarlılık Test Prosedürü (AI için)

Bir PR/commit’te şu sorular otomatik cevaplanmalı:

- [ ] Yeni semboller TYPES.md’ye eklendi mi?
- [ ] Yeni çıkarım “INFERENCE-RULES” ile uyumlu mu?
- [ ] Aksiyomlara dokunulduysa, “conservative extension” mi?
- [ ] Her proof, “kullanılan aksiyomlar + tip kontrol” içeriyor mu?
