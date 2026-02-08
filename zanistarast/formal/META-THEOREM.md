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
