Proje Genel Bakış
Bu proje, makine öğrenimi tekniklerini kullanarak müzik türlerini sınıflandırmayı amaçlamaktadır. Veri seti, çeşitli ses özellikleri ve parçaların tür etiketlerini içermektedir. Süreç, veri temizliği, keşifsel veri analizi (EDA), özellik ölçeklendirme, Ana Bileşen Analizi (PCA) kullanarak boyut indirgeme ve lojistik regresyon ile model eğitimi aşamalarını içermektedir.

İçerik

Veri Yükleme ve Keşif
Veri seti yüklenir ve bir kopyası oluşturulur.
Veri setinin ilk birkaç satırı ve temel bilgileri görüntülenir.
Eksik değerler ve benzersiz türler belirlenir.

Veri Görselleştirme
Müzik türlerinin dağılımı, bir sayım grafiği ile görselleştirilir.
Özellikler arasındaki ilişkileri anlamak için bir korelasyon matris oluşturulur.

Veri Ön İşleme
Eksik tür değerlerine sahip satırlar çıkarılır.
Kategorik özellikler sayısal değerlere dönüştürülür.

Boyut İndirgeme
Özellik seti standartlaştırılır.
PCA uygulanarak boyutlar azaltılır ve %80 varyans korunur.
Kümülatif açıklanan varyans görselleştirilir.

Model Eğitimi ve Değerlendirme
Hem orijinal hem de PCA ile dönüştürülmüş veriler üzerinde lojistik regresyon modelleri eğitilir.
Model performansı doğruluk ve sınıflandırma raporları ile değerlendirilir.

Bilinmeyen Türlerin Tahmini
Eksik tür bilgisine sahip kayıtlar izole edilir.
Eksik türler, daha iyi performans gösteren model ile tahmin edilir.

Sonuçlar ve Değerlendirme
Orijinal DataFrame, tahmin edilen türler ile güncellenir.
Güncellenmiş tür dağılımı görüntülenir.

Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olduğundan emin olun:
pip install pandas numpy scipy scikit-learn matplotlib seaborn

Kullanım
Reponuzu klonlayın veya indirin.
Koddaki yolun, veri seti dosyanıza işaret ettiğinden emin olun.
Veri yüklemeden model değerlendirmesine kadar tüm adımları gerçekleştirmek için betiği çalıştırın.

Örnek Çıktılar
Tür dağılımı ve özellik korelasyonu için görselleştirmeler.
Her iki model için doğruluk puanları.
Eksik türler için tahminler ile güncellenmiş DataFrame.

Not
Betiğin doğru çalışabilmesi için music_dataset_mod.csv veri setinin belirtilen yolda mevcut olduğundan emin olun.
Koddaki dosya yolunu, yerel veri seti konumunuza işaret edecek şekilde ayarlayın.

İletişim
Herhangi bir soru veya öneri için [Yiğit Can Sayar] ile [yigitcnsyr@gmail.com] üzerinden iletişime geçebilirsiniz.
