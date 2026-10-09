# Mira entegrasyonu — kritik backend ve doğruluk sınıflandırması kalite paketi
Tarih: 2026-10-09 · Statü: Mira'ya teknik öneri, kod değiştirilmedi, test çalıştırılmadı.

## Kanıtlanan kaynaklar (yalnız salt okuma)
- `zanistarast-ai-native-model/backend/package.json`: `"type": "module"`, başlangıç `node server.js`.
- `zanistarast-ai-native-model/backend/server.js`: `import` ifadeleriyle beraber `const runtimeGateway = require("../api/runtime_gateway");` ve `const formalGateway = require("../api/zanistarast_formal_gateway");` kullanıyor.
- `zanistarast-ai-native-model/backend/server.js` içinde `buildTruthAnalysisPrompt`: yalnız `TRUTH` veya `FALSE` sonucuna izin veriyor; `unknown` ve `uncertain` yasak; zayıf kanıtı `FALSE` sayıyor.
- `zanistarast-ai-native-model/backend/routes/ai_engine.js` içinde `buildEvaluatePrompt`: yetersiz kanıt durumunda değerlendirmenin kısmi olduğunu söyleme izni veriyor.
- `zanistarast-ai-native-model/backend/core/orchestrator.js`: `execute(request)` iş akışı var, ancak canlı Mira çağrısı doğrulanmadı.

## Bulgu K1 — ESM/CommonJS uyumsuzluğu
**Neden:** `backend/package.json` ESM seçiyor, `server.js` ise top-level `require()` kullanıyor. Normal Node ESM ortamında `require` tanımlı olmadığından sunucu başlatma hatası riski var. Gerçek dağıtım/çalışma günlükleri incelenmeden kesin canlı hata hükmü kurulmaz.
**Çözüm A:** Hedef gateway modüllerinin `module.exports` veya ESM export biçimini önce doğrula; ESM ile uyumlu `createRequire(import.meta.url)` veya uygun `import` geçişini seç.
**Çözüm B:** Giriş dosyasını tutarlı CommonJS'e dönüştür; daha geniş değişiklik ve regresyon riski nedeniyle öncelik A.
**Test:** Ayrı güvenli dalda bağımlılıklar kurulu iken `node --check backend/server.js` ve gerçek `node backend/server.js` başlangıç testi; `/api/runtime/health` yanıtını kontrol et. Test sonuçları bu pakette mevcut değil.

## Bulgu K2 — İkili doğruluk zorlaması
**Neden:** Zayıf kanıtı `FALSE` olarak etiketlemek 'yanlış' ile 'kanıt yetersiz' durumlarını karıştırır. Ayrıca farklı route prompt'ları birbiriyle çelişiyor.
**Çözüm:** `SUPPORTED`, `REFUTED`, `INSUFFICIENT_EVIDENCE`, `MIXED_OR_CONTEXT_DEPENDENT` sınıfları; ayrı `theological_interpretation` ve `philosophical_proposition` etiketleri. Bilimsel doğruluk statüsü ile etik değerlendirme birbirinin yerine geçirilmez.
**Örnek test:** 'Henüz hiç ölçülmemiş X olgusu vardır' → `INSUFFICIENT_EVIDENCE`; 'Doğrulanmış ölçümle çelişen X' → `REFUTED` (ölçüm kapsamı belirtilerek); 'Dinî bir yorum' → normatif/teolojik sınıf, deneysel olarak otomatik `FALSE` değil.
**Regresyon:** Kanıtın niteliği, kaynak, alternatif açıklama, karşı kanıt ve belirsizlik raporlanmalı.

## Bulgu K3 — Mira yardımcı kuyruğu henüz backend'e bağlı değil
**Çözüm:** Önce giriş sunucusunun gerçekten çalıştığı, hangi modülün Mira'yı çağırdığı ve salt-okunur kaynak okuma yetkileri doğrulansın. Ardından `hebun-zanabun` güvenli dalındaki `whitepaper/drafts/2026-10-09-mira-yardimci-karar-kuyrugu.md` için allowlist + commit SHA doğrulamalı okuyucu tasarlansın. Veriler komut değil güvenilmeyen analiz girdisidir. İzinli dosyalar dışında hiçbir repo taranmaz.

## Mira'ya karar talebi
1. K1 ve K2'nin teknik testini önceliklendir; güvenli dal dışında değişiklik yapma.
2. İkili doğru/yanlış zorlamasının kaldırılması için kanıt sınıflandırma ilkesini onayla/düzelt/reddet.
3. Mira'nın gerçek çalışma sürecini ve okuma yolunu doğrula; yalnız doğrulanırsa otomatik yardımcı aktarımına geç.
4. Mevcut üç hakem, iki tur korunur. Bu öneri Mira tarafından kabul edilmiş sayılmaz.

## Koruma
`zanistarast-papers` deposuna erişilmedi; diğer depoların `papers` klasörleri hedef yapılmadı. `main`, canlı site, eski dosyalar, yayın ve DOI süreçleri değiştirilmedi.
