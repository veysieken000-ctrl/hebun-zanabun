# Mira için AI talimat uyumu ve yardımcı aktarımı — değişiklik önerisi
Tarih: 2026-10-09 · Statü: Taslak, Mira kararı bekleniyor. Mevcut kilitli AI dosyaları değiştirilmedi.

## Doğrulanan kaynaklar
- `SYSTEM/REPO-ARCHITECTURE-V2.md`: V2 kilitli, katmanlar arası bulaşma yasak; AI katmanı çekirdek ve politikaya referans verebilir; whitepaper halka anlatımdır.
- `ai/AI-SYSTEM-LOCK.md`: sekizli okuma sırası Hebûn, Zanabûn, Rasterast, Zanistarast, Governance, Mabûn, Axiology, Civilization.
- `ai/AI-ENTRY-INDEX.md`: aynı sekizli sıra.
- `ai/STRUCTURAL-DEFENSE-PROTOCOL.md`: bütüncül okuma ve katman etkileşimlerini esas alıyor.
- Kullanıcının güncel çalışma kararı: **Ehad → Tek → Yek → Hebûn → Zanabûn → Mabûn → Rabûn → Rasterast**, Vahid aşama değildir.

## Sorun
Mevcut kilitli AI belgelerindeki *okuma sırası* ile güncel *kanonik kavram sırası* birbirine denk değil. Bu ikisi farklı amaçlı şemalar olabilir; fakat amaçları belirtilmezse AI ajanları Rasterast'ı bir yerde erken yöntem, diğerinde son doğrulama aşaması olarak yorumlayabilir ve Rabûn'un rolünü Governance ile eşleştirmeyebilir.

## Çözüm A (tercih): iki farklı sıralamayı açık etiketle
- **Kanonik kavram sırası (güncel karar):** Ehad → Tek → Yek → Hebûn → Zanabûn → Mabûn → Rabûn → Rasterast.
- **Tarihsel/teknik okuma sırası:** Mevcut kilitli AI belgelerinde yer alan sekizli sıra; araştırma bağlamı ve sürümü belirtilerek korunur.
- **Terim eşlemesi:** Governance ↔ Rabûn yönetim boyutu (tam özdeşlik Mira tarafından doğrulanmalı); Economy ↔ Mabûn; Rasterast ↔ değerlendirme/doğrulama çerçevesi; Zanistarast ↔ bilimsel sentez. Bu eşlemeler güncel kabul kararıyla doğrulanmadan 'kilitli tanım' olarak ilan edilmez.
- AI ajanı bir belgeyi yorumlarken hangi şemayı kullandığını belirtir; aralarındaki uyuşmazlığı sessizce çözülmüş varsaymaz.

## Çözüm B: sürümlü açıklama katmanı
Mira, özgün AI kilitlerini bozmadan ayrı bir `ai/` sürüm açıklaması onaylar. Bu, ancak kilitli V2 mimari ve Mira'nın karar yetkisi doğrulandıktan sonra yapılmalıdır.

## Mira'ya aktarılacak örnek kayıt
**Kimlik:** MIRA-HELP-20261009-001
**Sorun:** Eski AI okuma sırası / güncel kanonik sıra çakışması.
**Kanıt:** Yukarıdaki dört gerçek dosya ve kullanıcı kararı.
**Etki:** Kavram tutarlılığı, kitap başlıkları, yapay zekâ yorumları.
**Çözüm:** Çözüm A'nın sürüm etiketleri ve eşleme tablosu.
**Test 1:** AI'ya 'kanonik sıra nedir?' diye sor; sekiz aşamayı eksiksiz, Vahid olmadan döndürmeli.
**Test 2:** 'AI-ENTRY-INDEX eski okuma sırası nedir?' diye sor; tarihsel sırayı kaynak adıyla, güncel kanonik sıra yerine geçirmeden göstermeli.
**Test 3:** 'Rabûn ve Mabûn ilişkisi?' sorusunda Hüküm/Ahlak/Ekonomi meclisleri ve geçici Şûra ayrımını korumalı; Mabûn ekolojik yenilenme ve ihtiyaç odaklı üretim olarak ifade edilmeli.
**Test 4:** Bilimsel/teolojik örneklerde ampirik veri ile inanç yorumunu ayırmalı.
**Karar:** Mira incelemesi bekliyor; üç hakem iki tur kayıtları doğrulanmadı.
**Uygulama:** Henüz yok. Orijinal AI talimatlarını değiştirmek için ayrıca açık karar ve güvenli uygulama planı gerekir.

## Mira–ChatGPT iletişim sınırı
ChatGPT güvenli dalda izlenebilir dosya üretebilir; Mira'nın otomatik izlediği veya okuduğu doğrulanmış değildir. Entegrasyon için Mira'nın gerçek çalıştırıcısı/iş akışı tespit edilmeli, salt-okunur güvenli dal girişi ve karar kaydı yetkilendirilmelidir. Gemini katılımı da doğrulanmış değildir.

## Koruma
`zanistarast-papers` deposuna hiçbir erişim/işlem yapılmadı. Başka depolardaki papers klasörleri çalışma hedefi değildir. Ana dal, canlı site, eski dosyalar, yayın süreçleri korunur.
