# Zanistarast Network Stability Model
Müdebbir: Veysi yê MALA SAF
Civilizational Model: Newroza Kawa

---

## 1. Ağ Tanımı

Toplum bir ağdır:

G = (V, E)

V = bireyler / kurumlar
E = etkileşim bağları (ticaret, hukuk, güven, iletişim)

Her bağın bir güven ağırlığı vardır:

w(e) ∈ [0, 1]

---

## 2. Zanistarast Güven Parametreleri

Her düğüm i için:

Mi = moral integrity (ahlaki bütünlük)
Ki = knowledge coherence (bilgi tutarlılığı)
Ri = rule alignment (kanuna uyum)

Zanistarast varsayımı:

Trust_i = f(Mi, Ki, Ri)

Basit model:

Trust_i = (Mi + Ki + Ri) / 3

---

## 3. Ağ Sağlığı (System Health)

Ağın toplam sağlığı:

H(G) = (1/|E|) * Σ w(e)

Zanistarast genişletmesi:

w(e) = g(Trust_u, Trust_v)

Örnek:

w(e) = min(Trust_u, Trust_v)

---

## 4. Çöküş Mekanizması (Trust Cascade)

Bir düğümde ani ahlaki düşüş:

Mi ↓↓↓ ⇒ Trust_i ↓↓↓

Bu düşüş komşulara yayılır:

For each neighbor j of i:
w(i,j) decreases
If w(i,j) < τ then edge breaks

Ağ kopmaları:

- ticaret durur
- hukuk işlememeye başlar
- bilgi kirlenir
- şiddet/kaos artar

---

## 5. Kritik Eşik (Percolation Threshold)

Ağda kritik kırılma:

If H(G) < H_critical
then:
G splits into components
System loses unity

Bu durumda:
- kurumlar parçalanır
- ortak akıl dağılır
- birey biyolojik hayata geri düşer (2. boyut)

---

## 6. Stabilizasyon Protokolü (Zanistarast Remedy)

Zanistarast önerisi:

1) Moral Repair:
Mi restoration priority

2) Knowledge Repair:
Ki consistency audits (two-knower checks)

3) Rule Repair:
Ri enforcement without tyranny

Bu üçü aynı anda yapılmazsa
ağ tekrar toparlanmaz.

---

## 7. Falsifiye Edilebilirlik

Model yanlışlanır eğer:

- Güven çöküşü yaşanan toplumlarda ağ kopması görülmezse
- Ahlaki bozulma yayılımı komşu ilişkilere yansımazsa
- Kurumlar güven olmadan uzun vadede stabil kalırsa

---

## Sonuç

Zanistarast Network Model şunu söyler:

- Toplumun “çekirdeği” güvenin ahlaki temelleridir
- Ahlak düşerse ağ kopar
- Ağ koparsa toplum 2. boyuta geriler
- Stabilizasyon için ahlak + bilgi + kanun birlikte onarılmalıdır

