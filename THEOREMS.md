THEOREMS – Hedef Teoremler (ZCT)

## Th1 – Drift Monotonluğu (Tanım Teoremi)
**İfade:** λ azalırsa Drift artar.  
**Matematik:** Drift = 1 − λ, dolayısıyla λ₂ ≤ λ₁ ⇒ Drift(λ₂) ≥ Drift(λ₁).  
**Formal hedef:** Lean’da `drift_monotone` / `driftL` üzerinden ispat.

Durum: (ZCT.lean içinde var)
Lean karşılığı: formal/lean/ZCT.lean
---

## Th2 – λ=0 İhmal Teoremi
**İfade:** λ=0 ise karar H’yi tamamen ihmal eder.  
**Matematik:** Score₀(s,u) = E(s,u).  
**Formal hedef:** `scoreL_lambda0`.

Durum: (ZCT.lean içinde var)
Lean karşılığı: formal/lean/ZCT.lean
---

## Th3 – λ=1 Tam Katılım Teoremi
**İfade:** λ=1 ise karar H+E toplamına eşittir.  
**Matematik:** Score₁(s,u) = H(s,u)+E(s,u).  
**Formal hedef:** `scoreL_lambda1`.

Durum: (ZCT.lean içinde var)
Lean karşılığı: formal/lean/ZCT.lean
---

## Th4 – Uyum Artışı İlkesi (Model Hedefi)
**İfade:** λ arttıkça üst ölçü karara daha fazla katılır, drift azalır ve uyum potansiyeli artar.  
**Matematik hedefi:** λ₂ > λ₁ ⇒ Drift(λ₂) < Drift(λ₁).  
**Formal hedef:** Drift kısmı ispatlanır; “uyum” kısmı için ek varsayım gerekir.

Durum: hedef
Lean karşılığı: formal/lean/ZCT.lean
---

## Th5 – Çatışma Azalma Teoremi (Varsayıma Bağlı)
**İfade:** λ arttıkça çatışma azalır.  
**Not:** Bu teorem “H ve E aynı yönde uyumlu davranıyor” gibi ek bir varsayım olmadan genelde doğru değildir.

**Matematik hedefi (şartlı):**
Eğer bir durum sınıfında H ve E eylemlere aynı yönde tepki veriyorsa,
λ₂ > λ₁ ⇒ Conflict(λ₂) ≤ Conflict(λ₁).

**Formal hedef:** “uyumlu durum sınıfı” tanımı eklendikten sonra ispat.

Durum: hedef
Lean karşılığı: formal/lean/ZCT.lean
---

## Th6 – Yol Kayması Eşiği (Tanım)
**İfade:** Yol kayması, λ’nın belirli bir eşik altına düşmesiyle başlar.  
**Matematik:** Drift ≥ δ ⇔ λ ≤ 1−δ.  
**Formal hedef:** Eşik tanımı + basit lemma.

Durum: hedef
Lean karşılığı: formal/lean/ZCT.lean
---

## Th7 – Hayvan/İnsan Ayrımı (Modelleme Teoremi)
**İfade:** Hayvanlarda λ pratikte daha stabildir; insanda λ değişkendir ve baskı altında düşebilir.  
**Not:** Bu teorem “ampirik model”dir; formel ispat yerine test ve örneklerle doğrulanır.

Durum: hedef (EXAMPLES + TESTS)
Lean karşılığı: formal/lean/ZCT.lean

---

## Th1 – Drift Monotonluğu
İfade: λ azalırsa Drift artar.  
Matematik: Drift = 1 − λ  
Formal karşılık: drift_monotone (ZCT.lean)

---

## Th2 – λ=0 İhmal Teoremi
İfade: λ=0 ise karar H’yi ihmal eder.  
Matematik: Score₀(s,u) = E(s,u)  
Formal karşılık: scoreL_lambda0

---

## Th3 – λ=1 Tam Katılım Teoremi
İfade: λ=1 ise karar H+E’dir.  
Matematik: Score₁(s,u) = H(s,u)+E(s,u)  
Formal karşılık: scoreL_lambda1

---

## Th4 – Uyum Artışı İlkesi
İfade: λ arttıkça Drift azalır.  
Matematik: λ₂ > λ₁ ⇒ Drift(λ₂) < Drift(λ₁)  
Formal karşılık: driftL + monotonicity

---

## Th5 – Çatışma Azalma (Varsayıma Bağlı)
İfade: Uyumlu durumlarda λ artışı çatışmayı azaltır.  
Not: Ek varsayım gerektirir.  
Formal hedef: Genişletilecek.

---

## Th6 – Yol Kayması Eşiği
İfade: Drift ≥ δ ⇔ λ ≤ 1−δ  
Formal hedef: Eşik lemma (eklenecek).

---

## Th7 – Hayvan/İnsan Ayrımı (Modelleme)
İfade: λ stabilitesi türsel farklılık gösterir.  
Not: Ampirik/model düzeyinde.


