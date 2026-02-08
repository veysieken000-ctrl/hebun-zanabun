# LOCK PROTOCOL — Freeze Rules (v1)

Bu dosya “sistem kilidi”dir.
Amaç: çekirdeğin sarsılmaması.

---

## 1) Kilitli Dosyalar (Değişim kurallı)

- AXIOMS.md
- TYPES.md
- INFERENCE-RULES.md
- CONSISTENCY.md
- META-THEOREM.md

Bu dosyalarda değişiklik yapılırsa:
- sebep yazılacak
- “neden muhafazakâr genişleme” olduğu açıklanacak
- tutarlılık kontrolü eklenecek

---

## 2) Serbest Dosyalar (Genişletilebilir)

- THEOREMS.md
- proofs/T*.md
- Whitepaper metinleri
- Rasterast/Mabûn vb. uygulama metinleri

---

## 3) Formal Kabul Şartı (En küçük standart)

Bir proof dosyası şu başlıkları taşımazsa kabul edilmez:

- İddia
- Kullanılan aksiyomlar
- Kullanılan çıkarım kuralları
- Tip notu (en azından kritik semboller)

---

## 4) Versiyonlama

- v1.x: çekirdeği kırmadan büyütme
- v2.0: ancak çekirdek değişirse (çok nadir)
