# PROOF DISCIPLINE — Zanistarast Derivation Rules (v1)

Amaç:
Teoremler sezgisel değil,
türetim kurallarıyla üretilsin.

Bu belge kanıtın nasıl yapılacağını tanımlar.

---

## 1) Geçerli Kanıt Türleri

Bir teorem yalnızca şu yollarla üretilebilir:

1. Aksiyom referansı (Ai)
2. Tanım genişletme
3. Mantıksal çıkarım (→, ∧, ∨, ¬)
4. Tip uyumluluk kontrolü
5. Boyut projeksiyon kontrolü

Bunlar dışında çıkarım geçersizdir.

---

## 2) Boyut Geçiş Kuralı

Bir üst boyut ifadesi:

𝔹₆

doğrudan

𝔹₂

üzerinde hüküm üretmez.

Ara projeksiyon gereklidir:

proj_6→5  
proj_5→4  
proj_4→3  
...

Aksi durumda kanıt reddedilir.

---

## 3) Normatif Üretim Kuralı

Normatif sonuç (ℕ𝕆) üretmek için:

★ operatörü zorunludur.

Eğer ★ yoksa:

Sonuç = bağlayıcı değildir.

---

## 4) Çelişki Eliminasyonu

Eğer bir sistem durumunda:

p ∧ ¬p

oluşursa:

- Sistem ⊥ durumuna geçer
- Tüm normatif çıkarımlar askıya alınır

Bu, A7’nin uygulamasıdır.

---

## 5) İki-Bilen Doğrulama Kuralı

Bir bilgi iddiası:

Know(x)

ancak aşağıdaki durumda bilimsel statü kazanır:

∃y ≠ x : confirm(y, Know(x)) = true

Tek özne doğrulaması epistemik bağlayıcılık üretmez.

---

## 6) Kanıt Ağacı Formatı

Her teorem şu biçimde yazılmalıdır:

1. Varsayım
2. Kullanılan aksiyom(lar)
3. Ara çıkarımlar
4. Sonuç
5. Tip kontrolü doğrulaması

---

## 7) Sistem Güvenlik İlkesi

Bir teorem:

- Aksiyom referansı olmadan
- Tip kontrolü yapılmadan
- Boyut geçişi belirtilmeden

geçerli sayılmaz.

---

Bu belge sistemin matematiksel omurgasını güçlendirir.

Zanistarast artık:

- Aksiyomatik
- Tip kontrollü
- Çıkarım kurallı
- Normatif kapı korumalı

bir yapıdadır
