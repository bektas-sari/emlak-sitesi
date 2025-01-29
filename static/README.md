# Emlak Sitem (Python/Flask Kullanılarak DeepSeek Ai Kod Editörünün yardımıyla Oluşturulmuştur)

Emlak Sitem, kullanıcıların satılık, kiralık ve günlük kiralık emlak ilanlarını kolayca bulabileceği bir web uygulamasıdır. Flask framework'ü kullanılarak geliştirilmiştir.

## Özellikler

- **Ana Sayfa:** Öne çıkan ilanlar, kategoriler ve arama motoru.
- **Hakkımızda:** Şirket bilgileri ve misyonumuz.
- **Projeler:** Devam eden ve tamamlanan projeler.
- **İletişim:** Kullanıcıların bize ulaşabileceği iletişim formu.
- **Admin Paneli:** Mesajları yönetmek için basit bir admin paneli (gelecek sürümde).

## Teknolojiler

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Veritabanı:** SQLite
- **Diğer Araçlar:** Jinja2 (Templating), SQLAlchemy (Veritabanı Yönetimi)

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler

- Python 3.8 veya üzeri
- Pip (Python paket yöneticisi)

### Adım 1: Projeyi Klonlayın

```bash
git clone https://github.com/bektas-sari/emlak_sitem.git
cd emlak_sitem

### Adım 2: Sanal Ortam Oluşturun ve Etkinleştirin
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

### Adım 3: Gerekli Paketleri Yükleyin
pip install -r requirements.txt

### Adım 4: Veritabanını Başlatın
python init_db.py

### Adım 5: Uygulamayı Çalıştırın
python app.py

Uygulama, http://127.0.0.1:5000/ adresinde çalışacaktır.

### Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.