# MNIST Rakam Üretici
PCA ve Kernel Density ile el yazısı rakamlar üreten, FastAPI ile servis eden, Docker ile kullanıma hazır ML projesi.

## Hakkında
GAN veya VAE gibi derin öğrenme mimarilerine ihtiyaç duymadan, boyut indirgeme ve istatistik yöntemleri ile yapay el yazısı görseller üretmek amaçlanmıştır.
* **Teknik:** PCA ile boyut indirgeyip, KDE ile yeni örnekler oluşturarak bunları görsellere dönüştürmek.
* **API:** FastAPI üzerinden anlık görsel üretimi.
* **Docker:** Docker ile ortamdan bağımsız mimari.
* **Görseller:** GitHub Actions altyapısı ile belirli aralıklarla otomatik olarak yeni görseller üretilip README sayfasına işlenir.
### Oluşturulmuş Resimler
![oluşturulmuş görüntü](assets/asset-1.png)
![oluşturulmuş görüntü](assets/asset-2.png)
![oluşturulmuş görüntü](assets/asset-3.png)
![oluşturulmuş görüntü](assets/asset-4.png)


## 🛠️ Teknolojiler ve Kütüphaneler

* **Dil:** Python 3.12
* **Makine Öğrenmesi:** Scikit-Learn (PCA, KernelDensity), NumPy, Joblib
* **Görselleştirme & Görüntü İşleme:** Matplotlib
* **Web API Framework:** FastAPI
* **Konteynerizasyon:** Docker
* **CI/CD & Otomasyon:** GitHub Actions