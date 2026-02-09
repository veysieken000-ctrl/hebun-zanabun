# META-THEOREM — System Lock Theorem (v1)

Amaç:
Sistemi “yorum savaşından” korumak:
- Ne eklenebilir?
- Ne eklenemez?
- Hangi şartta teorem geçerlidir?

---

## MT1 — Soundness under Typing (Tip altında sağlamlık)

S = (A, R, T) olsun.

Önerme:
Eğer bir teorem τ,
- sadece A’daki aksiyomları kullanıyorsa,
- sadece R’deki çıkarım kurallarıyla türetilmişse,
- ve her adım T ile tip doğrulamasından geçmişse,

o zaman τ “formal olarak geçerli” kabul edilir.

Kısa ifade:
Type-Checked Proof ⇒ Accepted Theorem

Bu, “hakikatin metafiziği” değil,
formal sistemin “iç geçerlilik kilidi”dir.

---

## MT2 — Conservative Extension Lock (Muhafazakâr genişleme kilidi)

Yeni aksiyom seti A' eklenmek istenirse:

Şart:
A' eklenince eski dilde (eski sembollerle) yeni bir çelişki üretilemez
ve eski teoremler “anlam kayması”na uğramaz.

Yani:
S ⊬ ⊥ ve S' ⊬ ⊥
ve eski dilde:
S' yeni bir “eski dil teoremi” üretip sistemi bozmaz.

Bu kilit şunu sağlar:
Sistem büyür ama çekirdek kırılmaz.

---

## MT3 — Dual-Kilit Zorunluluğu (Ahlak–Hüküm birlikte)

Normatif bağlayıcılık üretmek için:

★(𝕍, 𝕁) yoksa bağlayıcı sonuç yoktur.

Bu meta-kural,
“salt biyoloji / salt zihin / salt kanun” ile
nihai norm üretmeyi engeller.

---

## Uygulama Notu (AI için)

Bir dosya “formal” etiketi alacaksa,
şu üç şeyi taşımak zorunda:

1) Tip listesi
2) Kullanılan çıkarım kuralları
3) Aksiyom referansları

# META-THEOREM — Layered Science Lock (v1)

Müdebbir: Veysi yê MALA SAF

## Amaç
Zanistarast formal katmanını "sarsılmaz çekirdek" olarak kilitlemek:
- Bilim = üst-perspektiften okuma
- İkili sistem = üçüncü referans olmadan kapanmaz
- Katmanlar arası indirgeme çelişki üretir

---

## MT1 — Üst-Perspektif Zorunluluğu (System Lock)

**İddia (MT1):**  
Her doğrulama/karar/teori üretimi için sistem dışı bir referans (üst-perspektif) zorunludur.

### Formal
S = (x,y) ikili yapı olsun.

1) Doğrulama operatörü: `Verify(·)`  
2) İç sistemde her ifade `φ` için `φ ∈ S` kabul edilsin.

**MT1:**
> `Verify(φ)` ancak `∃z : z ∉ S ∧ Observes(z,S)` ise mümkündür.

### Kullanılan aksiyomlar
- A5 (İki-bilen şartı)
- A6 (Nesnel referans)
- A7 (Tutarlılık)
- A12 (Dual kilit: ahlak★hüküm)
- A13 (Üst-perspektif aksiyomu)

### Sonuç
- Bilim içe kapanamaz.
- Katmanların üstten okunması zorunludur.
- İndirgemeci “tek katman” bilim iddiası sistemsel olarak eksiktir.

---

## MT1’in Sistem Kilidi Etkisi
- Hebûn (ontoloji) → katman tanımı sağlar
- Zanabûn (epistemoloji) → doğrulama şartını koyar
- Zanistarast formal katman → “üst-perspektif” zorunluluğunu kilitler

Bu kilit bozulursa sistem çelişkiye düşer (A7).
