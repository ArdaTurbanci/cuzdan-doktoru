https://ethverify.streamlit.app/
<p align="center">
  <h1>ethverify</h1>
  <p align="center">Ethereum adreslerinin güvenilirliğini anında doğrulayın ve dijital varlıklarınızı koruyun.</p>
  <p align="center">
    <img alt="Build Status" src="https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge&logo=github">
    <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/ardaturbanci/ethverify?style=for-the-badge&color=yellow">
  </p>
</p>

---
## DEMO:

> https://ethverify.streamlit.app/
> 
## 🚀 Projenin Stratejik Önemi

> Kripto para ekosisteminde, özellikle Ethereum ağında, dolandırıcılık ve kötü niyetli adresler önemli bir risk oluşturmaktadır. Kullanıcılar, bilinmeyen veya şüpheli adreslere varlık gönderirken büyük maddi kayıplarla karşılaşabilirler. Mevcut doğrulama yöntemleri genellikle yetersizdir veya teknik bilgi gerektirir, bu da güvenli işlem yapmayı zorlaştırır.

`ethverify`, bu kritik soruna kapsamlı ve kullanıcı dostu bir çözüm sunar. Makine öğrenimi destekli analizlerle Ethereum adreslerinin güvenilirliğini anında değerlendirerek, kullanıcıların potansiyel dolandırıcılık girişimlerinden korunmasına yardımcı olur. Bu sayede, dijital varlıklarınızı güvenle yönetebilir, bilinçli kararlar alabilir ve kripto dünyasındaki riskleri minimize edebilirsiniz.

## ✨ Temel Özellikler

`ethverify` projesi, Ethereum adres doğrulamasını basitleştiren ve güvenliği artıran bir dizi güçlü özellik sunar:

*   🔍 **Anında Adres Doğrulama**: Girilen Ethereum adreslerinin geçerliliğini ve geçmişini hızla kontrol edin.
*   🚨 **Şüpheli Aktivite Tespiti**: Makine öğrenimi modelleri (`cuzdan_doktoru_model.pkl`) sayesinde potansiyel dolandırıcılık veya kötü niyetli adresleri proaktif olarak belirleyin.
*   🛡️ **Güvenlik Analizi**: Adreslerle ilişkili risk puanlarını ve detaylı güvenlik raporlarını kolayca görüntüleyin, bilinçli kararlar alın.
*   🌐 **Kullanıcı Dostu Arayüz**: `app.py` ile sunulan sezgisel web arayüzü sayesinde teknik bilgi gerektirmeden kolayca sorgulama yapın ve sonuçları anlayın.
*   ⚡ **Gerçek Zamanlı Veri Entegrasyonu**: En güncel blockchain verileriyle sürekli güncel ve doğru doğrulama sonuçları elde edin (varsayımsal).
*   📊 **Detaylı Raporlama**: Bir adresin geçmiş işlem hacmi, etkileşimleri ve bilinen risk faktörleri hakkında kapsamlı bilgiler edinin.

## 🏗️ Teknik Mimari

`ethverify` projesi, sağlam ve ölçeklenebilir bir yapı üzerine inşa edilmiştir.

### Teknoloji Yığını

| Teknoloji           | Amaç                                            | Temel Fayda                                           |
| :------------------ | :---------------------------------------------- | :---------------------------------------------------- |
| **Python**          | Ana geliştirme dili, veri işleme, model yürütme | Esneklik, geniş kütüphane desteği, hızlı prototipleme |
| **scikit-learn**    | Makine öğrenimi modeli eğitimi ve tahmini      | Güçlü ML algoritmaları, kolay entegrasyon             |
| **Flask / Streamlit** | Basit web arayüzü veya API sunumu (`app.py`)    | Hızlı web uygulaması geliştirme, kullanıcı erişimi    |
| **Pip / Venv**      | Bağımlılık yönetimi ve izole ortam              | Proje bağımlılıklarının kolay yönetimi                |

### Dizin Yapısı

Projenin anlaşılır ve düzenli bir yapısı vardır:

```
.
├── 📁 .devcontainer/         # Geliştirme ortamı yapılandırmaları
├── 📄 app.py                 # Ana uygulama dosyası (web arayüzü/API)
├── 📄 cuzdan_doktoru_model.pkl # Eğitilmiş makine öğrenimi modeli (cüzdan analizi)
├── 📄 model_columns.pkl      # Model için gerekli sütun bilgileri
├── 📄 README.md              # Proje açıklaması ve dokümantasyon
└── 📄 requirements.txt       # Proje bağımlılıkları listesi
```

## 🛠️ Operasyonel Kurulum

`ethverify` projesini yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin.

### Ön Gereksinimler

Başlamadan önce sisteminizde aşağıdaki yazılımların kurulu olduğundan emin olun:

*   **Python 3.8+** (Tercihen en son kararlı sürüm)
*   **pip** (Python paket yöneticisi)
*   **etherscan API_KEY**
### Kurulum Adımları

Projenin kurulumu oldukça basittir:

1.  **Depoyu Klonlayın**:
    ```bash
    git clone https://github.com/ardaturbanci/ethverify.git
    cd ethverify
    ```

2.  **Sanal Ortam Oluşturun**:
    Proje bağımlılıklarını izole etmek için bir sanal ortam (`venv`) oluşturmanız önerilir:
    ```bash
    python3 -m venv venv
    ```

3.  **Sanal Ortamı Etkinleştirin**:
    *   **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```
    *   **Windows (Command Prompt)**:
        ```bash
        venv\Scripts\activate.bat
        ```
    *   **Windows (PowerShell)**:
        ```bash
        venv\Scripts\Activate.ps1
        ```

4.  **Bağımlılıkları Yükleyin**:
    Gerekli tüm Python paketlerini `requirements.txt` dosyasından yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
    API anahtarınızı gerekli yerlere yazın.

5.  **Uygulamayı Çalıştırın**:
    Kurulum tamamlandıktan sonra, uygulamayı başlatabilirsiniz:
    ```bash
    python app.py
    ```
    Uygulama genellikle `http://127.0.0.1:5000` adresinde çalışacaktır. Tarayıcınızdan bu adresi ziyaret ederek `ethverify` arayüzüne erişebilirsiniz.
