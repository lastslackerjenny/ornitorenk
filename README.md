# Emlak Oyunu

Bu proje, Monopoly benzeri basit bir emlak ticareti oyunudur. Oyuncular zar atarak oyun tahtasında ilerler, mülkler satın alır ve rakiplerinden kira toplar. Hedef, diğer oyuncuları iflas ettirmek ve en zengin oyuncu olmaktır.

## Kurulum

Gerekli bağımlılıkları yüklemek için:

```bash
npm install
```

Oyunu başlatmak için:

```bash
npm start
```

## Oyun Kuralları

1. Oyun başladığında, her oyuncu 1500₺ ile oyuna başlar.
2. Sırayla zar atarak oyun tahtasında ilerlenir.
3. Bir oyuncu sahipsiz bir mülk karesine geldiğinde, o mülkü satın alabilir.
4. Bir oyuncu, başka bir oyuncuya ait bir mülk karesine geldiğinde, o mülkün kira bedelini sahibine öder.
5. Başlangıç noktasından geçen oyuncu 200₺ kazanır.
6. Oyuncular iflas ettiğinde oyundan çıkar. Son kalan oyuncu kazanır.

## Özellikler

- 2 oyunculu oyun desteği
- 40 kareden oluşan oyun tahtası
- Farklı renk gruplarında mülkler
- Başlangıç, şans, kamu fonu, vergi ve diğer özel kareler

## Teknolojiler

- React
- Vite
- CSS

## Gelecekteki Geliştirmeler

- 3 ve 4 oyunculu oyun desteği
- Şans ve kamu fonu kartları
- Ev ve otel inşa etme sistemi
- Oyuncular arası mülk ticareti
- Daha gelişmiş UI/UX 