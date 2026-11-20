# Dış çizgiden sonra 34 px'te ince kalan kelime görselleri

İlya'nın 9/10 raporundaki öneriyle 238 kelime görseline 1,05 birimlik #17132B dış çizgi verildi.
Bunlar çizgiyle de ince ya da boş kalıyordu. Tablodakilerin hepsi `sanat/kelime-gorsel-uret.py` ile kalın biçimlerle yeniden çizildi
(`data/kelime-gorsel.json`); istenirse Gemini'den daha zengin parçalar alınabilir.

**Gemini'ye tek istem:** "Tek bir nesne, düz renk, eşit kalınlıkta koyu (#17132B) dış çizgi, yuvarlak hatlar, yüzsüz, yazısız,
saydam zemin, 32x32 simge okunurluğunda kalın biçimler: <nesne>."

| Kelime | Şimdiki görsel | Sorun | İstenecek nesne |
|---|---|---|---|
| observe | teleskop | ayaklar ~1 px | kısa, kalın ayaklı teleskop |
| increase, improve, rate, gradual, significant, increasingly | yükselen çizgi grafiği | ince çizgi, boş zemin | kalın yükselen üç sütun ve ok |
| reduce, decrease | düşen çizgi grafiği | aynı | kalın alçalan üç sütun ve ok |
| relate, relevant, depend on | ataş / zincir | ince tel | kalın iki halka |
| give up | beyaz dikdörtgen | boş görünüyor | kalın direkli beyaz bayrak |
| vary, level | ince sürgüler | ince çizgiler | kalın kaydırma düğmeli sürgü |
| rapid | ince rüzgâr | çizgiler | kalın hız çizgili koşan ayakkabı |
