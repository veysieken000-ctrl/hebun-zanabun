# OPERATORS — Typing & Semantics (v1)

Amaç: “⊗ ne demek?” tartışması bitmeli.

## 1) Tip Sistemi (özet)
- 𝔹: varlık
- 𝕂: bilgi nesnesi
- 𝕍: değer/ahlak kısıtları
- 𝔻₆: boyut etiketi

## 2) Operatörler

### ⊕ (merge)
- Tip: (T × T) → T
- Anlam: aynı tipte iki nesnenin tek temsil altında birleşmesi.
- Örn: iki bilgi kaynağının ortaklaştırılması.

### ⊗ (composition)
- Tip: (A × B) → C (C bağlama göre)
- Anlam: “iki farklı katman” etkileşimi ile yeni yapı üretir.
- Örn: (bilgi ⊗ değer) → normatif karar

### ◁ (normlama)
- Tip: (𝕂 × 𝕍) → 𝕂
- Anlam: bilgi, değer kısıtlarıyla sınırlandırılır; ‘keyfi bilgi’ engellenir.

### ★ (dual-lock: Ahlak + Hüküm)
- Tip: (karar × (ahlak,hüküm)) → bağlayıcı-sonuç
- Anlam: Ahlak ve hükmün birlikte kilitleyici olması (ikili sistem gereği).

## 3) Yasaklar
- Tip uyuşmazlığına izin yok.
- Aynı sembol iki farklı işlemde kullanılmaz.
3) Tip sistemi (x nedir? varlık mı? bilgi mi?)

# OPERATORS — Formal Operator Definitions (v1)

Amaç:
İşlemler matematiksel netlikte.

---

## ⊕ (Merge)

Tip: (T × T) → T  
Aynı tip birleşimi.

---

## ⊗ (Composition)

Tip: (A × B) → C  
Katmanlar arası üretim.

Örnek:
Bilgi ⊗ Değer → Normatif yapı

---

## ◁ (Normlama)

Tip: (𝕂 × 𝕍) → 𝕂  
Bilgi, değer filtresinden geçirilir.

---

## ★ (Dual Lock)

Tip: (Ahlak × Hüküm) → Binding

İkili sistem gereği:
Ahlak + Hüküm birlikte bağlayıcıdır.

---

## Yasak

- Tip dışı işlem yok.
- Aynı sembol iki işlemde kullanılmaz.
Buraya kadar temel formal çekirdek tamamlandı.
