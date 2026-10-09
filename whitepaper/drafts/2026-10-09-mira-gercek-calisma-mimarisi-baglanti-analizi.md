# Mira çalışma mimarisi: doğrulanmış giriş noktaları ve güvenli bağlantı önerisi
Tarih: 2026-10-09 · Durum: Mira'ya öneri; entegrasyon kurulmadı, kod çalıştırılmadı.

## Doğrulanan dosyalar (salt okuma)
**Kaynak depo:** `veysieken000-ctrl/zanistarast-ai-native-model`, main (hiçbir değişiklik yapılmadı).
- `.github/workflows/zanistarast_autonomous_pulse.yml` ve `.github/workflows/zanistarast-autonomous_pulse.yml`: aynı isimli iki GitHub Actions tanımı; `push main` ve `workflow_dispatch` ile bilimsel/test betiklerini çağırıyor. Yardımcı taslak kuyruğu okuma adımı yok. Çalıştırılmış/başarılı oldukları bu dosyalardan anlaşılamaz.
- `backend/core/orchestrator.js`: reasoning → planning → executor/verification → decision → optimization → simulation → response → learning sırasını tanımlıyor; giriş `execute(request)`. Bu, çağrılan bir yazılım modülü; Mira'nın aktif süreç olarak kullandığı doğrulanmadı.
- `core/zanistarast_orchestrator.py`: içeriği Python programı değil, metin olarak iş akışı/klasör şeması. Çalışan Mira entegrasyonu kanıtı değildir.
- `reference-implementation/mira/src/zanistarast_scientific_mission.rs`: Mira için bilimsel misyonu Rust veri yapısı olarak tanımlıyor; doğrudan sohbet/mesaj teslim arayüzü değil. Karşı kanıtı koruma, sonuçtan geriye kanıt üretmeme ve özgün bilimsel katkı ilkeleri var.
- `constitution/07-beneficial-agent-protocol.md`: doğrulama temelli, manipülasyondan uzak yararlı ajan koordinasyonunu tarif ediyor; entegrasyon kodu değil.
**Hedef depo:** `veysieken000-ctrl/hebun-zanabun`, `SYSTEM/REPO-ARCHITECTURE-V2.md` kilitli katman sınırlarını belirliyor.

## Teknik çıkarım
Mira'ya güvenli aktarım için *aday* giriş noktası `backend/core/orchestrator.js` modülünün `execute(request)` arayüzüdür; ancak çalışma zamanı, Mira'ya bağlı olup olmadığı, API şeması, yetkiler ve dağıtım doğrulanmadığı için otomatik bağlantı kurulmuş sayılmaz. GitHub Actions 'Autonomous Pulse' Mira'nın kendisiyle eş tutulamaz.

## Somut bağlantı tasarımı (uygulama değil)
1. **Girdi:** Sadece `hebun-zanabun` güvenli dalındaki `whitepaper/drafts/2026-10-09-mira-yardimci-karar-kuyrugu.md` ve onun referans verdiği izinli yardımcı dosyalar.
2. **Koruma:** `zanistarast-papers` deposuna hiçbir istek gönderme. Başka depolardaki `papers` klasörlerine de erişme. GitHub okuma token'ı yalnız açıkça izinli repo/dal/yollara sınırla.
3. **Doğrulama:** URL, commit SHA, içerik hash'i, dosya yolu ve güvenli dal eşleşmesini denetle; kaynak dışı talimatları yetkili komut olarak çalıştırma.
4. **Ayrıştırma:** Yardımcı öneriyi `request.text` içine doğrudan sınırsız talimat olarak değil, **güvenilmeyen araştırma girdisi** olarak aktar. İnsan/Mira karar alanlarını ChatGPT doldurmaz.
5. **İşleme:** Mira'nın gerçekten çalışan arayüzü teyit edilirse öneriyi onun mevcut üç hakemli iki turlu karar kuyruğuna sun. Kaynak, çözüm, test, karşı kanıt ve risk alanları zorunlu olsun.
6. **Çıktı:** Ayrı izinli güvenli dalda yeni bir karar kayıt dosyası; `status: received/reviewed/accepted/rejected` değerleri yalnız gerçek işleme kanıtıyla yazılır. Varsayılan `status: pending`.
7. **Test:** Sahte kayıt, değiştirilmiş SHA, yasak repo yolu, bozuk kaynak, aynı kayıt tekrar teslimi, iki farklı sürüm ve çevrimdışı Mira senaryolarında yanlış kabul/yanlış yetki verilmediğini kontrol et.
8. **Yayın:** Mira'nın açık kararı ve doğrulama olmadan main, canlı site, yayın, DOI veya dergi başvurusu yapılmaz.

## Saptanan ek kalite sorunu
İki GitHub Actions dosyası aynı `name`, tetikleyici ve test adımlarını içeriyor. Bu durum yinelenen iş akışı riski yaratır; fakat gerçekten iki kez koştuğu loglarla doğrulanmadan kesin hüküm kurulmaz. **Çözüm:** Mira önce gerçek workflow run kayıtlarını ve hangi tanımın kullanıldığını kontrol etsin; sonra güvenli dalda birleştirme önerisini değerlendirsin. Bu çalışma kapsamında mevcut dosyalar değiştirilmedi.

## Bekleyen doğrulamalar
- Mira'nın aktif dağıtımı ve çağrı yolu.
- `backend/core/orchestrator.js` modülünü hangi süreç çağırıyor?
- Mira'nın dosya okuma ve karar kayıt yetkisi var mı?
- Güvenli dal değişikliklerini hangi periyotla takip ediyor?
- Üç hakem ve iki tur gerçek değerlendirme kayıtları nerede?

## Koruma ve epistemik durum
Bu belge bir teknik keşif ve öneridir. Mira'nın yeni dosyaları aldığına veya işlediğine dair kayıt yoktur. `zanistarast-papers` deposuna dokunulmadı. Ana dal, orijinal metinler ve canlı site değiştirilmedi.
