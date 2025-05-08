# Monopoly Oyunu - Ürün Gereksinimleri Dokümanı (PRD)

**Proje Adı:** Ornitorenk
**Sürüm:** 0.1
**Tarih:** 8 Mayıs 2025
**Proje Sahibi:** LastSlackerJenny

## 1. Giriş ve Amaç

Bu doküman, geliştirilecek olan Monopoly oyununun temel gereksinimlerini, özelliklerini ve hedeflerini tanımlamaktadır. Amacımız, klasik Monopoly deneyimini dijital platforma taşıyarak eğlenceli ve rekabetçi bir oyun ortamı sunmaktır.

## 2. Hedef Kitle

* Klasik kutu oyunlarını sevenler
* Arkadaşlarıyla veya ailesiyle çevrimiçi oyun oynamak isteyenler
* Strateji ve şans oyunlarından hoşlanan her yaştan kullanıcı

## 3. Genel Bakış

Oyun, oyuncuların zar atarak oyun tahtasında ilerlediği, mülkler satın aldığı, kiraladığı, ticaret yaptığı ve rakiplerini iflas ettirmeye çalıştığı klasik Monopoly kurallarına dayanacaktır.

## 4. Özellikler

### Yapıldı

    * Temel oyun konsepti belirlendi.
    * PRD dokümanının ilk taslağı oluşturuldu.

### Yapılacak

**4.1. Temel Oyun Mekanikleri**
    * [ ] Oyun Tahtası Tasarımı ve Uygulaması
        * [ ] Klasik Monopoly tahtasına sadık dijital tasarım
        * [ ] Mülkler, Şans ve Kamu Fonu kartları, Vergiler, Başlangıç noktası, Kodese Gir/Ziyaret, Bedava Otopark gibi standart karelerin yerleşimi
    * [ ] Oyuncu Hareketleri
        * [ ] Zar atma mekaniği (2 adet 6 yüzlü zar)
        * [ ] Zarların sonucuna göre piyonların tahtada ilerlemesi
        * [ ] Çift zar atıldığında tekrar zar atma hakkı (arka arkaya 3 çift zarda kodese girme)
    * [ ] Mülk Yönetimi
        * [ ] Mülk satın alma
        * [ ] Mülk üzerine ev/otel kurma (set tamamlandığında)
        * [ ] Mülk kiralama (diğer oyuncular mülke geldiğinde kira toplama)
        * [ ] Mülk ipotek etme/ipotekten çıkarma
        * [ ] Mülk ticareti (oyuncular arası)
    * [ ] Para Yönetimi
        * [ ] Başlangıç parası dağıtımı
        * [ ] Gelir (kira, başlangıçtan geçiş vb.) ve gider (vergi, ceza, kira ödeme vb.) takibi
    * [ ] Şans ve Kamu Fonu Kartları
        * [ ] Dijital kart desteleri
        * [ ] Kart çekme mekaniği
        * [ ] Kartlarda belirtilen aksiyonların (para kazanma/kaybetme, belirli bir kareye gitme, hapisten bedava çıkma kartı vb.) uygulanması
    * [ ] Kodese Girme ve Çıkma Mekanikleri
        * [ ] Kodese girme koşulları (direkt gitme, 3 çift zar, kart ile)
        * [ ] Kodesten çıkma seçenekleri (para ödeme, zar atma, hapisten bedava çıkma kartı kullanma)
    * [ ] Oyun Sonu Koşulları
        * [ ] Bir oyuncu hariç tüm oyuncuların iflas etmesi
        * [ ] Belirlenen tur sayısı veya süre sonunda en zengin oyuncunun kazanması (opsiyonel oyun modu)
    * [ ] Oyuncu Sayısı
        * [ ] Minimum ve maksimum oyuncu sayısı belirleme (örn: 2-4 oyuncu)

**4.2. Kullanıcı Arayüzü (UI) ve Kullanıcı Deneyimi (UX)**
    * [ ] Ana Menü (Yeni Oyun, Oyuna Katıl, Ayarlar, Çıkış)
    * [ ] Oyun İçi Arayüz
        * [ ] Oyun tahtasının net görünümü
        * [ ] Oyuncu piyonları ve mevcut konumları
        * [ ] Her oyuncunun para miktarı ve sahip olduğu mülklerin listesi
        * [ ] Zar atma butonu
        * [ ] Mülk satın alma/kiralama/ipotek etme/ev-otel kurma arayüzleri
        * [ ] Ticaret teklifi arayüzü
        * [ ] Şans/Kamu Fonu kartı gösterim alanı
        * [ ] Oyun içi mesajlar ve bildirimler (kimin sırası, ne oldu vb.)
        * [ ] Oyun geçmişi/logları (opsiyonel)
    * [ ] Ayarlar Menüsü (Ses, Grafik, Oyun Kuralları varyasyonları vb.)
    * [ ] Kullanıcı dostu ve sezgisel navigasyon

**4.3. Çok Oyunculu (Multiplayer) Özellikler (Eğer hedefleniyorsa)**
    * [ ] Yerel Çok Oyunculu (Tek cihazda birden fazla oyuncu)
    * [ ] Çevrimiçi Çok Oyunculu
        * [ ] Oyun lobisi oluşturma/listeleme
        * [ ] Arkadaş davet etme sistemi
        * [ ] Sunucu tarafı oyun yönetimi
        * [ ] Oyuncular arası senkronizasyon
        * [ ] Sohbet özelliği (opsiyonel)

**4.4. Yapay Zeka (AI) (Eğer tek oyunculu mod hedefleniyorsa)**
    * [ ] Farklı zorluk seviyelerinde yapay zeka rakipler
    * [ ] Yapay zekanın mülk satın alma, ticaret yapma, ev/otel kurma gibi kararları alabilmesi

**4.5. Grafik ve Ses**
    * [ ] Çekici ve temaya uygun görsel tasarım
    * [ ] Piyon, zar, kart, bina vb. modellemeleri/görselleri
    * [ ] Arka plan müziği ve ses efektleri (zar atma, para sesi, kart çekme vb.)

**4.6. Platformlar**
    * [ ] Hedeflenen platformlar (örn: PC (Windows, macOS, Linux), Mobil (Android, iOS), Web)

**4.7. Opsiyonel/Gelecek Özellikler (Sürüm 1.0 sonrası için)**
    * [ ] Farklı temalı oyun tahtaları ve piyonlar
    * [ ] Özelleştirilebilir oyun kuralları
    * [ ] Başarımlar (Achievements)
    * [ ] Liderlik tabloları (Leaderboards)
    * [ ] Oyun içi satın almalar (kozmetik vb. - dikkatli planlanmalı)
    * [ ] Farklı diller için yerelleştirme

## 5. Teknik Gereksinimler (Gerekirse)

* **Oyun Motoru:** [Belirlenen oyun motoru, örn: Unity, Unreal Engine, Godot veya özel bir motor]
* **Programlama Dili:** [Kullanılacak programlama dilleri, örn: C#, C++, GDScript, JavaScript]
* **Veritabanı (Çevrimiçi oyunlar için):** [Kullanılacak veritabanı türü]
* **Sunucu Altyapısı (Çevrimiçi oyunlar için):** [Sunucu barındırma detayları]

## 6. kilometre Taşları ve Takvim (Örnek)

* **Sprint 1 (Tarih Aralığı):** Temel oyun mekanikleri (zar atma, piyon hareketi, mülk satın alma) prototipi.
* **Sprint 2 (Tarih Aralığı):** Kullanıcı arayüzü temelleri, Şans/Kamu Fonu kartları.
* **Sprint 3 (Tarih Aralığı):** Çok oyunculu altyapısı (eğer varsa) veya AI temelleri.
* **Alfa Sürümü (Hedef Tarih):**
* **Beta Sürümü (Hedef Tarih):**
* **Yayın Tarihi (Hedef Tarih):**

## 7. Riskler ve Çözüm Önerileri

* **Risk:** Çok oyunculu senkronizasyon sorunları.
    * **Çözüm:** Kapsamlı testler, güvenilir ağ kütüphaneleri kullanımı.
* **Risk:** Yapay zekanın dengesiz olması (çok kolay veya çok zor).
    * **Çözüm:** Farklı algoritmalar denemek, oyunculardan geri bildirim almak.
* **Risk:** Proje süresinin uzaması.
    * **Çözüm:** Gerçekçi planlama, görevlerin önceliklendirilmesi, MVP (Minimum Viable Product - Minimum Uygulanabilir Ürün) yaklaşımı.

## 8. Açık Kalan Konular / Sorular


* Hangi platforma öncelik verilecek?
* Oyun içi ekonomi ne kadar affedici/cezalandırıcı olmalı?