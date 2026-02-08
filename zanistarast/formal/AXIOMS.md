# AXIOMS — A1..A12 (v1)

Bu aksiyomlar: Hebûn (ontoloji) + Zanabûn (epistemoloji) + ikili sistem (ahlak-hüküm) kilidini formal yapar.

## Ontoloji (Hebûn)
A1 (Katmanlılık): 𝔻₆ = {1..6} ve her varlık x için dim(x) ∈ 𝔻₆ vardır.
A2 (Alt-üst bağımlılık): d<e ise, e-boyutun işletimi d-boyut verilerini kapsar. (d ⊑ e)
A3 (Geçiş): x → y ilişkisi yalnızca tipler uyumluysa kurulabilir.

## Epistemoloji (Zanabûn)
A4 (İki-bilen şartı): “bilgi” statüsü için en az iki bağımsız onay kanalı gerekir: K = (k₁ ⊕ k₂) ve çelişkisizlik şartı.
A5 (Tutarlılık): Çelişik bilgi bilgi değildir: (k ⟂ k) ⇒ ¬Valid(k)
A6 (Sınır): Her bilgi önerisi falsifiye edilebilirlik / doğrulanabilirlik sınırıyla etiketlenmelidir.

## Ahlak + Hüküm (İkili kilit)
A7 (Dual-lock): Normatif sonuçlar yalnızca ★ ile bağlayıcı olur: ψ ancak (ahlak,hüküm) birlikte kilitlenirse 𝕁 üretir.
A8 (Hak-merkez): Adalet/hak, normatif sistemin merkezi ölçütüdür (𝕍 içinde birincil kısıt).

## Okuma/Davet (Rasterast dili)
A9 (Akla hitap): Her ana iddia φ için akıl kanalıyla test edilebilir bir biçim (E1-E3) verilir.
A10 (Vicdana hitap): Her normatif ψ için değer kısıtı (𝕍) açık yazılır.
A11 (Fıtrata hitap): İnsanın varlık sahasını daraltan sistemler “alt-boyut sabitlemesi” üretir.
A12 (Yol ayrımı): Alt-boyut sabitlemesi sürdürülebilir değildir; çöküş dinamiği üretir.
5) Teorem kataloğu + Proof’lar (T1, T2, …)

# AXIOMS — Zanistarast Axiom System (v1.1)

Amaç:
Sistem sezgisel değil, aksiyomatik olarak temellidir.
Bu aksiyomlar modelin indirgenemez çekirdeğini oluşturur.

---

# I. Ontolojik Aksiyomlar

A1 — Boyut Tanımlılığı  
Her varlık en az bir boyutta tanımlıdır.

∀x ∈ 𝔹, ∃d ∈ 𝔻₆ : dim(x) = d

---

A2 — Üst Boyut İndirgenemezliği  
Üst boyut alt boyuta tam indirgenemez.

∀d_i, d_j ∈ 𝔻₆ :
(d_i > d_j) ⇒ ¬(d_i ⊆ d_j)

---

A3 — Projeksiyon Tanımlılığı  
Her üst boyut alt boyuta projekte edilebilir.

∀x ∈ 𝔹, ∀d_i > d_j :
∃ proj_{d_j}(x)

---

A4 — Ontolojik Dualite  
Her belirgin varlık bir zıt referansla anlam kazanır.

∀x ∈ 𝔹, ∃y ∈ 𝔹 : Opp(x, y)

---

# II. Epistemolojik Aksiyomlar

A5 — İki-Bilen Gerekliliği  
Doğrulanmış bilgi en az iki özne gerektirir.

Know(x) ⇒ ∃y ≠ Self : Confirm_y(x)

---

A6 — Nesnel Referans Zorunluluğu  
Bilgi öznel kapalı sistem değildir.

∀k : Valid(k) ⇒ ∃r ∈ ℝ : Ref(k, r)

---

A7 — Tutarlılık Aksiyomu  
Çelişki içeren sistem bilgi üretmez.

(x ∧ ¬x) ⇒ ⊥

---

A8 — Yanlışlanabilirlik Sınırı  
Her model sınır içerir.

∀M : ∃Boundary(M)

---

# III. Ahlaki Aksiyomlar

A9 — Varlık Koruma Eğilimi  
Her öz varlığını korumaya yönelir.

∀x ∈ 𝕍 : Preserve(x)

---

A10 — Varlık Genişleme Eğilimi  
Her bilinçli öz varlık alanını genişletmek ister.

∀x ∈ Conscious ⊂ 𝕍 : Expand(x)

---

A11 — Normatif Filtre  
Norm bağlayıcılığı için bilgi ve değer birlikte gerekir.

Norm(x) ⇒ (x ∈ 𝕂 ∧ x ∈ 𝕍)

---

# IV. Hüküm Aksiyomu

A12 — Dual Norm Kilidi  
Bağlayıcı norm için ahlak ve hüküm birlikte gereklidir.

Binding(x) ⇒ (Moral(x) ∧ Judgment(x))
