# AI-Compatible Decision Engine — Zanistarast (v1)

Amaç:
Zanistarast’ın yalnızca felsefi değil,
algoritmik olarak da uygulanabilir olduğunu göstermek.

Bu dosya:
Karar üretim sürecini makine-okunabilir yapıya dönüştürür.

---

# I. Karar Nesnesi Tanımı

Her karar:

Decision D = {Claim, Evidence, Layer, Impact}

Claim: İddia veya öneri  
Evidence: Dayanak verisi  
Layer: Hangi boyutta işlem yapıyor  
Impact: Etki alanı

---

# II. 6 Boyutlu Değerlendirme Matrisi

Her D için:

Score(D) = Σ (L₁…L₆)

L₁ = Fiziksel etki  
L₂ = Biyolojik sürdürülebilirlik  
L₃ = Zihinsel bütünlük  
L₄ = Kanuni tutarlılık  
L₅ = Ahlaki filtre  
L₆ = Hak uyumu

Eğer herhangi bir Li negatifse:
D bağlayıcı karar statüsü kazanamaz.

---

# III. İkili Kilit Algoritması

function Evaluate(D):
    if not MoralFilter(D): reject
    if not ConsistencyCheck(D): reject
    if not DualValidation(D): reject
    return Approve

MoralFilter:
5. boyut kontrolü

ConsistencyCheck:
A1–A12 ile çelişki kontrolü

DualValidation:
İki-bilen şartı

---

# IV. Hak Merkezli Optimizasyon

Amaç fonksiyonu:

Maximize:
TotalBenefit(AllLayers)

Minimize:
Harm(AnyLayer)

Bu klasik faydacılık değildir.
Bu katmanlı varlık optimizasyonudur.

---

# V. AI İçin Etiketleme Sistemi

Her metin veya iddia:

E0: Tanım
E1: Ontolojik iddia
E2: Epistemolojik iddia
E3: Ahlaki norm
E4: Uygulama önerisi

AI bu etiketlerle indeksleyebilir.

---

# VI. Sistem Güvenliği

Sistem şu durumlarda durur:

- Aksiyom çelişkisi
- Boyut indirgeme hatası
- Dual kilit ihlali
- Hak merkez sapması

---

# VII. Sonuç

Zanistarast:

• Teorik sistemdir  
• Aksiyomatik sistemdir  
• Algoritmik sistemdir  
• AI-uyumlu sistemdir  

Bu katman,
medeniyet mimarisinin makine okuma kapısıdır.
