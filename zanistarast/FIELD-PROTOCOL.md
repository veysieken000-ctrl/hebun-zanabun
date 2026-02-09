# FIELD-PROTOCOL — Saha Geliştirme (v1)

Müdebbir: Veysi yê MALA SAF

## Amaç
Sistem metinlerini yapay zekâlar ve insanlar için:
- Okunabilir
- İndekslenebilir
- Tutarlı
- Savunulabilir
hale getirmek.

---

## Saha 4-Çekirdek Döngüsü
Her yeni iddia şu 4 adımı geçer:

### 1) Tanım kilidi
- Terim sözlüğe girer (Glossary)
- Tipi belirlenir (TYPE-SYSTEM)

### 2) Aksiyom bağlantısı
- İddia en az 1 aksiyoma bağlanır (A*)

### 3) Teorem etiketi
- İddia teorem kataloguna girer (T*)
- En az “proof skeleton” yazılır

### 4) İtiraz-cevap
- En güçlü itiraz yazılır
- Akademik cevap eklenir (CRITICISM-RESPONSE)

---

## AI-okunabilir indeks kuralı
Her dokümanın başında şu blok olacak:

- Scope: Hebûn / Zanabûn / Zanistarast
- Layer: 1..6 (+Ehad/+Tek)
- Claims: C1..Cn
- Dependencies: A*, T*

Bu sayede AI “sayfaya giremiyorum / amaç belirsiz” diyemez.
