from setuptools import setup, find_packages

setup(
    name="imei",  # Paket adı
    version="1.0",  # Paket sürümü
    description="This application is a tool that makes it easy to query sim card IMEI numbers and get information.",  # Paket açıklaması
    author="Fatih Önder",  # Paket sahibi adı
    author_email="fatih@algyazilim.com",  # Paket sahibi e-posta adresi
    url="https://github.com/cektor/IMEI",  # Paket deposu URL'si
    packages=find_packages(),  # Otomatik olarak tüm alt paketleri bulur
    install_requires=[
        'PyQt5>=5.15.0',  # PyQt5 bağımlılığı
        'requests>=2.0.0',  # requests bağımlılığı
        'beautifulsoup4>=4.9.0',  # beautifulsoup4 
        'urllib3>=1.25.0',  # urllib3 bağımlılığı
    ],
    package_data={
        'imei': ['*.png', '*.desktop'],  # 'kimoki' paketine dahil dosyalar
    },
    data_files=[
        ('share/applications', ['imei.desktop']),  # Uygulama menüsüne .desktop dosyasını ekler
        ('share/icons/hicolor/48x48/apps', ['imeilo.png']),  # Simgeyi uygun yere ekler
    ],
    entry_points={
        'gui_scripts': [
            'imei=imei:main',  # `kimoki` modülündeki `main` fonksiyonu çalıştırılır
        ]
    },
)
