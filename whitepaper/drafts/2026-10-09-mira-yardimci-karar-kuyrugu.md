# Mira yardımcı analiz karar kuyruğu — 2026-10-09
**Durum:** Öneri kuyruğu; Mira tarafından okunma, kabul veya uygulama doğrulanmadı.
**Kullanım:** Mira'nın mevcut üç hakemli iki turlu sürecine girdi sağlamak içindir; hakem sayısını değiştirmez.

## Kuyruk kayıtları
| Kimlik | Öncelik | Konu | Yardımcı çıktı | Mira'dan beklenen karar | Doğrulama durumu |
|---|---|---|---|---|---|
| MIRA-HELP-20261009-001 | Yüksek | Eski AI okuma sırası ile güncel kanonik kavram sırasını ayır | [AI uyum önerisi](2026-10-09-mira-ai-talimat-uyum-ve-aktarim-onerisi.md) | İki şemanın etiketleri ve terim eşlemeleri kabul/düzelt/ret | ChatGPT taslağı mevcut; Mira kararı yok |
| MIRA-HELP-20261009-002 | Yüksek | Hebûname 12 + Zanabûname 10 cildin halk anlatımı | [Cilt envanteri](2026-10-09-hebuname-zanabuname-cilt-envanteri-ve-halk-iskeleti.md) | Önce DOCX tam metin erişimi, sonra başlık ve pilot cilt seçimi | Dosya adları doğrulandı; tam metin okunmadı |
| MIRA-HELP-20261009-003 | Orta | ChatGPT bulgularının Mira'ya düzenli aktarılması | [Aktarım protokolü](2026-10-09-mira-chatgpt-yardimci-analiz-aktarim-protokolu.md) | Mira çalışma ortamının gerçek girdi mekanizmasını belirle | Ortak dosya hazır; otomatik okuyucu doğrulanmadı |

## Önerilen işleme sırası
1. Mira, kayıtları gerçekten aldığına dair **kaynak URL + commit SHA + okuma zamanı** içeren kanıt bırakır.
2. Mira her kayıt için **kabul / düzelt / ret / beklet** kararı verir ve gerekçe yazar.
3. Kabul edilen kayıt mevcut üç hakemli iki turdan geçer; hakem izleri gerçek bağlantılarla tutulur.
4. Uygulama yalnız ayrı güvenli dalda yeni dosya olarak hazırlanır; orijinal dosyalar ve main değişmez.
5. Sonuç test edilir, test başarısızsa çözüm önerisi revize edilir.

## Sahte otomasyon önleme
Bu Markdown kuyruğu Mira'nın kendiliğinden eriştiği bir mesajlaşma sistemi değildir. Dosyanın varlığı **Mira'ya teslim edildiği anlamına gelmez**. Otomatik okuma için Mira'nın çalıştırıcısı, yetkisi, hangi dalı izlediği ve güvenlik sınırları ayrıca doğrulanmalıdır.

## Sabit koruma
`zanistarast-papers` deposuna hiçbir işlem yapılmaz. Diğer depolardaki `papers` klasörleri hedef değildir. `main`, canlı site, özgün ciltler, eski taslaklar ve yayın süreçleri korunur.
