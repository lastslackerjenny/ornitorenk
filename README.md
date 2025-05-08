# Monopoly Oyunu

Bu proje, klasik Monopoly masa oyununun Python dilinde basit bir uygulamasıdır.

## Özellikler

- 2-4 oyuncu arasında oynanabilen basit bir konsol Monopoly oyunu
- Zar atma, mülk satın alma, kira ödeme, ipotek etme gibi temel mekanikler
- Şans ve Kamu Fonu kartları
- Kodes mekanikleri (kodese girme ve çıkma)
- İflas yönetimi
- Tam oyun döngüsü (Oyuncuların sırayla oynadığı, en son bir kazanan olana kadar)

## Kurulum

1. Python 3.6 veya daha yüksek sürümü yükleyin.
2. Bu depoyu klonlayın veya zip olarak indirin:
   ```
   git clone https://github.com/kullaniciadi/monopoly-oyunu.git
   ```
3. Proje klasörüne gidin:
   ```
   cd monopoly-oyunu
   ```

## Oyunu Çalıştırma

Ana oyunu çalıştırmak için:

```
python main.py
```

## Proje Yapısı

```
.
├── main.py               # Ana giriş noktası
├── src/                  # Kaynak kod klasörü
│   ├── __init__.py       # Paket tanımı
│   ├── game.py           # Ana oyun mantığı
│   └── models/           # Model sınıfları
│       ├── __init__.py   # Paket tanımı
│       ├── player.py     # Oyuncu sınıfı
│       ├── property.py   # Mülk sınıfı
│       └── board.py      # Tahta sınıfı
└── README.md             # Bu dosya
```

## Gelecek Özellikler

- Grafik arayüz (GUI)
- Daha kapsamlı oyun tahtası (tüm 40 kare)
- Çevrimiçi çok oyunculu mod
- Yapay zeka rakipler
- Özelleştirilebilir oyun kuralları

## Lisans

Bu proje açık kaynaklıdır.

## Katkıda Bulunanlar

- LastSlackerJenny (Proje Sahibi) 