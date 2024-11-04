import pandas as pd
import numpy as np
import scipy

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score 
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# 1. Verinin yuklenmesi ve kopya olusturulmasi
df = pd.read_csv('C:\\Users\\yigit\\Desktop\\music\\music_dataset_mod.csv')  # veri yolu belirtildi
df_copy = df.copy()

# 2. Veri setinin ilk birkac satirina goz atilmasi 
print(df_copy.head())

# 3. Veri setinin genel bilgilerinin incelenmesi 
print(df_copy.info())

# 4. Eksik degerlerin belirlenmesi 
print(df_copy.isnull().sum())

# 5. Genre kolonundaki benzersiz türlerin kesfedilmesi 
benzersiz_turler = df_copy['Genre'].unique()
print("Benzersiz türler:", benzersiz_turler)
print("Benzersiz tür sayısı:", len(benzersiz_turler))

# 6. Genre kolonunun dagiliminin gorsellestirilmesi 
plt.figure(figsize=(12, 6))
sns.countplot(data=df_copy, x='Genre', order=df_copy['Genre'].value_counts().index)
plt.xticks(rotation=45)
plt.title('Müzik Türlerinin Dağılımı')
plt.xlabel('Tür')
plt.ylabel('Sayım')
plt.show()

# 7. Genre kolonundaki null değerlerin cikrailmasi ve yeni bir DataFrame olusturulmasi 
df_clean = df_copy.dropna(subset=['Genre']).reset_index(drop=True)

# 8. Tüm kategorik sutunların etiket kodlayici ile sayısal değerlere cevirilmesi 
categorical_columns = df_clean.select_dtypes(include=['object']).columns
label_encoder = LabelEncoder()
for col in categorical_columns:
    df_clean[col] = label_encoder.fit_transform(df_clean[col])

# 9. Korelasyon matrisinin olusturulmasi ve ısı haritası olarak gorsellestirilmesi
correlation_matrix = df_clean.corr()
plt.figure(figsize=(14, 12))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Özellikler Arası Korelasyon Matrisi ve Hedef Değişken')
plt.show()

# 10. Verinin standardize edilmesi
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_clean.drop('Genre', axis=1))  # Genre hedef değisken olduğu için cikarilmasi
y_encoded = df_clean['Genre']

# 11. PCA olusturulmasi ve veri setine uygulanmasi
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# 12. Aciklanan varyans oraninin analiz edilmesi
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance_ratio)
components_needed = np.argmax(cumulative_variance >= 0.80) + 1  # En az %80'ini yakalayan bilesen sayisi

# 13. Kumulatif varyansin gorsellestirilmesi
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='--')
plt.axhline(y=0.80, color='r', linestyle='-')
plt.xlabel('Bileşen Sayısı')
plt.ylabel('Kümülatif Açıklanan Varyans')
plt.title('Kümülatif Açıklanan Varyans Grafiği')
plt.grid()
plt.show()

print(f"%80 varyansı yakalamak için gerekli bileşen sayısı: {components_needed}")

# 14. Secilen bilesen sayisi ile PCA'nin tekrar uygulanmasi
pca_optimal = PCA(n_components=components_needed)
X_pca_optimal = pca_optimal.fit_transform(X_scaled)

# 15. Modeli PCA tabanli ve orijinal verilerle değerlendirilmesi
# PCA tabanli model
X_train_pca, X_test_pca, y_train, y_test = train_test_split(X_pca_optimal, y_encoded, test_size=0.3, random_state=42)
log_reg_pca = LogisticRegression(max_iter=10000)
log_reg_pca.fit(X_train_pca, y_train)
y_pred_pca = log_reg_pca.predict(X_test_pca)

# Performans degerlendirmesi
accuracy_pca = accuracy_score(y_test, y_pred_pca)
print("PCA Tabanlı Model Doğruluğu:", accuracy_pca)
print(classification_report(y_test, y_pred_pca))

# Orijinal model
X_train_orig, X_test_orig, y_train_orig, y_test_orig = train_test_split(X_scaled, y_encoded, test_size=0.3, random_state=42)
log_reg_orig = LogisticRegression(max_iter=10000)
log_reg_orig.fit(X_train_orig, y_train_orig)
y_pred_orig = log_reg_orig.predict(X_test_orig)

# Performans degerlendirmesi
accuracy_orig = accuracy_score(y_test_orig, y_pred_orig)
print("Orijinal Model Doğruluğu:", accuracy_orig)
print(classification_report(y_test_orig, y_pred_orig))

# 16. Bilinmeyen tur verisinin izole edilmesi
unknown_genre_data = df_copy[df_copy['Genre'].isnull()].reset_index(drop=True)

# 17. Verinin hazırlanmasi
X_unknown = unknown_genre_data.drop('Genre', axis=1)
X_unknown_scaled = scaler.transform(X_unknown)  # Olcekleme
X_unknown_pca = pca_optimal.transform(X_unknown_scaled)  # PCA donusumu

# 18. Model ile tahmin yapilmasi
if accuracy_pca > accuracy_orig:
    predicted_genres_encoded = log_reg_pca.predict(X_unknown_pca)
else:
    predicted_genres_encoded = log_reg_orig.predict(X_unknown_scaled)

# 19. Tahminlerin orijinal etiketlere donusturulmesi
predicted_genres = label_encoder.inverse_transform(predicted_genres_encoded)

# 20. Orijinal DataFrame'in guncellenmesi
df_copy.loc[df_copy['Genre'].isnull(), 'Genre'] = predicted_genres

# 21. Guncellenmis DataFrame'in incelenmesi
print(df_copy.head())
print("Güncellenmiş Genre dağılımı:")
print(df_copy['Genre'].value_counts())

# 22. Projenin Quiz sorusunu cevaplamak icin yazdigim kod
predicted_genre_992 = df_copy.loc[992, 'Genre']
print(f"Track 992'nin tahmin edilen türü: {predicted_genre_992}")
