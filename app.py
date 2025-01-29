from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

# Flask uygulamasını oluştur
app = Flask(__name__)
app.secret_key = 'gizli_bir_anahtar'  # Flash mesajları için gerekli

# Veritabanı dosyası yolu
DATABASE = 'emlak.db'

# Veritabanı bağlantısı oluştur
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Veritabanını başlat
def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit()
        conn.close()

# Örnek ilanlar
ilanlar = [
    {"id": 1, "baslik": "Satılık Daire", "konum": "İstanbul", "tip": "satilik", "aciklama": "Merkezi konumda satılık lüks daire."},
    {"id": 2, "baslik": "Kiralık Villa", "konum": "İzmir", "tip": "kiralik", "aciklama": "Deniz manzaralı kiralık villa."},
    {"id": 3, "baslik": "Günlük Kiralık Yazlık", "konum": "Bodrum", "tip": "gunluk-kiralik", "aciklama": "Günlük kiralık yazlık ev."},
    {"id": 4, "baslik": "Yeni Proje", "konum": "Ankara", "tip": "projeler", "aciklama": "Yeni proje kapsamında satılık daireler."},
]

# Ana sayfa için route (yol) tanımla
@app.route('/')
def home():
    return render_template('index.html')

# Hakkımızda sayfası için route (yol) tanımla
@app.route('/about')
def about():
    return render_template('about.html')

# Projeler sayfası için route (yol) tanımla
@app.route('/projects')
def projects():
    return render_template('projects.html')

# İletişim sayfası için route (yol) tanımla
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Veritabanına kaydet
        conn = get_db_connection()
        conn.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)',
                     (name, email, message))
        conn.commit()
        conn.close()

        flash('Mesajınız başarıyla gönderildi!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

# Arama sonuçları için route (yol) tanımla
@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    results = [ilan for ilan in ilanlar if query in ilan['baslik'].lower() or query in ilan['konum'].lower()]
    return render_template('search.html', results=results, query=query)

# Filtreleme için route (yol) tanımla
@app.route('/filter/<type>')
def filter(type):
    results = [ilan for ilan in ilanlar if ilan['tip'] == type]
    return render_template('filter.html', results=results, type=type)

# İlan detay sayfası için route (yol) tanımla
@app.route('/ilan/<int:ilan_id>')
def ilan_detay(ilan_id):
    ilan = next((ilan for ilan in ilanlar if ilan['id'] == ilan_id), None)
    if ilan:
        return render_template('ilan_detay.html', ilan=ilan)
    else:
        return "İlan bulunamadı.", 404

# Uygulamayı çalıştır
if __name__ == '__main__':
    init_db()  # Veritabanını başlat
    app.run(debug=True)