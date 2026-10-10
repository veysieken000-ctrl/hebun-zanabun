# Mira çalıştırma kabul kapısı — 2026-10-10

**Statü:** Teknik bulgu ve doğrulama planı. Canlı kurulum/çalıştırma tamamlandı iddiası değildir.

## Doğrulanmış mevcut mimari
- PWA `reference-implementation/mira-pwa/config.js` API: `https://zanistarast-papers.onrender.com`.
- Rust API `reference-implementation/mira-api/src/main.rs`: `/health`, `/tasks`, `/background-work`, `/tracking`, `/sessions`; başlangıçta `start_zanistarast_foundation_bootstrap` çağrılıyor.
- `DATABASE_URL` yoksa sohbet oturumları yalnız RAM'de. `tracking_records` ve `background_work` başlangıçta RAM vektörleri; kalıcı veri doğrulanmadı.
- Render dağıtım kaydı `live` olmakla birlikte HTTP sağlık yanıtı ve bilimsel görev sonucu ayrı doğrulanmalıdır.
- Ayrı güvenli dalda `mira-tools/review_evidence_gate.py`, `test_review_evidence_gate.py` ve `probe_mira_api.py` oluşturuldu.

## Öncelikli uygulama sırası
1. Salt okunur canlı `GET /health` kontrolü: gerçek `service=zanistarast-mira-api,status=ok` cevabı olmadan geçme.
2. Kimlik doğrulaması: Müdebbir gizli anahtarı yalnız sunucu ortam değişkeninde; değerleri loglara, repoya, sohbete aktarma.
3. Kalıcılık: Render PostgreSQL bağlantısı ve restart sonrası sohbet, görev, tracking ve background-work kayıtlarının korunmasını test et. Yeni şema eklenmeden önce mevcut şema/migration ve eski veri yedeğini doğrula. Veri kaybı riski varsa deploy yapma.
4. Mevcut başlatma görevinin çıktılarını `run_id`, gerçek zaman, kaynak, hash, hata, süre ve durumla kaydet; sadece görev oluşturulması PASS değildir.
5. Güvenli kaynak allowlist'iyle yardımcı kuyruk okuma köprüsü; kaynağı yetkili komut değil, araştırma girdisi olarak işle. SHA ve tekrar-işleme kontrolü yap.
6. Üç hakem × iki tur: her turda ayrı `run_id`, kaynak, değerlendirme, itiraz ve revizyon izi. Hakem kimlikleri aynı modelse gerçek bağımsızlık iddia etme.
7. Kanıt kapısı `review_evidence_gate.py` ile altı kayıt ve revizyon kaydı denetimi; gerçek hakemlik kalitesini ayrıca denetle.
8. Tam regresyon: eski oturumlar, PWA giriş/çıkış, görev, tracking, 32 faz işlevleri ve kilitli talimatlar. Yalnız yeşilse dağıtım için ayrı onay al.

## Kesin durdurma koşulları
- Canlı API yanıtı yok, kimlik doğrulama kırılıyor veya eski veri kaybı riski varsa.
- Hakem raporu/scheduler sonucu yalnız metin olarak üretilmiş, log veya kanıt URI'si yoksa.
- Korunan depolara veya başka depolardaki `papers` klasörlerine erişim gerekiyorsa: kapsamı yeniden açıkça onaylat.
- `main`, canlı servis, mevcut dosya veya yayın işlemi değişecekse ayrıca açık onay al.

## Kabul
`API_OK` + `PERSISTENCE_OK` + `RUN_PROVEN` + `SIX_REVIEW_RECORDS` + `REGRESSION_GREEN`. Bu beş ölçüt ayrı ayrı kanıtlanmadıkça Mira otonom çalışıyor denmez.
