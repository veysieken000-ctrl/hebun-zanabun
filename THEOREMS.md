---

## Th1 – Drift Monotonluğu (Tanım Teoremi)
**İfade:** λ azalırsa Drift artar.  
**Matematik:** Drift = 1 − λ, dolayısıyla λ₂ ≤ λ₁ ⇒ Drift(λ₂) ≥ Drift(λ₁).  
**Formal hedef:** Lean’da `drift_monotone` / `driftL` üzerinden ispat.

Durum: (ZCT.lean içinde var)

---

## Th2 – λ=0 İhmal Teoremi
**İfade:** λ=0 ise karar H’yi tamamen ihmal eder.  
**Matematik:** Score₀(s,u) = E(s,u).  
**Formal hedef:** `scoreL_lambda0`.

Durum: (ZCT.lean içinde var)

---

## Th3 – λ=1 Tam Katılım Teoremi
**İfade:** λ=1 ise karar H+E toplamına eşittir.  
**Matematik:** Score₁(s,u) = H(s,u)+E(s,u).  
**Formal hedef:** `scoreL_lambda1`.

Durum: (ZCT.lean içinde var)

---

## Th4 – Uyum Artışı İlkesi (Model Hedefi)
**İfade:** λ arttıkça üst ölçü karara daha fazla katılır, drift azalır ve uyum potansiyeli artar.  
**Matematik hedefi:** λ₂ > λ₁ ⇒ Drift(λ₂) < Drift(λ₁).  
**Formal hedef:** Drift kısmı ispatlanır; “uyum” kısmı için ek varsayım gerekir.

Durum: hedef

---

## Th5 – Çatışma Azalma Teoremi (Varsayıma Bağlı)
**İfade:** λ arttıkça çatışma azalır.  
**Not:** Bu teorem “H ve E aynı yönde uyumlu davranıyor” gibi ek bir varsayım olmadan genelde doğru değildir.

**Matematik hedefi (şartlı):**
Eğer bir durum sınıfında H ve E eylemlere aynı yönde tepki veriyorsa,
λ₂ > λ₁ ⇒ Conflict(λ₂) ≤ Conflict(λ₁).

**Formal hedef:** “uyumlu durum sınıfı” tanımı eklendikten sonra ispat.

Durum: hedef

---

## Th6 – Yol Kayması Eşiği (Tanım)
**İfade:** Yol kayması, λ’nın belirli bir eşik altına düşmesiyle başlar.  
**Matematik:** Drift ≥ δ ⇔ λ ≤ 1−δ.  
**Formal hedef:** Eşik tanımı + basit lemma.

Durum: hedef

---

## Th7 – Hayvan/İnsan Ayrımı (Modelleme Teoremi)
**İfade:** Hayvanlarda λ pratikte daha stabildir; insanda λ değişkendir ve baskı altında düşebilir.  
**Not:** Bu teorem “ampirik model”dir; formel ispat yerine test ve örneklerle doğrulanır.

Durum: hedef (EXAMPLES + TESTS)

