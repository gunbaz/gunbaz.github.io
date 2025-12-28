# Veri Defteri

Yapay Zeka ve Veri Mühendisliği öğrencileri için hazırlanmış teknik ders notları ve dokümantasyon sitesi.

🔗 **[gunbaz.github.io](https://gunbaz.github.io)**

## Hakkında

Bu proje, üniversite müfredatındaki dersleri sadece syntax seviyesinde değil, bilgisayar mimarisi ve sistem tasarımı perspektifinden ele alan bir kaynak oluşturmayı hedefler.


## Teknik Altyapı

| Bileşen | Teknoloji |
|---------|-----------|
| Dokümantasyon Motoru | [MkDocs](https://www.mkdocs.org/) |
| Tema | [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) |
| Matematik Render | MathJax (LaTeX) |
| Görselleştirme | Matplotlib |
| Hosting | GitHub Pages |

## Yerel Geliştirme

```bash
# Repository'yi klonla
git clone https://github.com/gunbaz/gunbaz.github.io.git
cd gunbaz.github.io

# Bağımlılıkları yükle
pip install -r requirements.txt

# Yerel sunucuyu başlat
mkdocs serve
```

Site varsayılan olarak `http://127.0.0.1:8000` adresinde çalışır.

## Proje Yapısı

```
.
├── docs/                   # Markdown kaynak dosyaları
│   ├── 1. Sinif/
│   ├── 2. Sinif/
│   ├── 3. Sinif/
|   └── 4. Sinif/
├── mkdocs.yml              # Site konfigürasyonu
└── requirements.txt        # Python bağımlılıkları
```

## Katkıda Bulunma

Hata bildirimi veya öneri için [Issues](https://github.com/gunbaz/gunbaz.github.io/issues) bölümünü kullanabilirsin.

## Lisans

Bu proje eğitim amaçlı oluşturulmuştur.
