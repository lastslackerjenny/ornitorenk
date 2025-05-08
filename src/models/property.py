class Property:
    def __init__(self, name, price, rent_base, group, position):
        self.name = name
        self.price = price
        self.rent_base = rent_base  # Temel kira
        self.group = group  # Mülk grubu (renk grubu)
        self.position = position  # Tahta üzerindeki pozisyon
        self.owner = None
        self.houses = 0
        self.hotel = False
        self.is_mortgaged = False
        
    def calculate_rent(self):
        """Mülkün kirasını hesaplar."""
        if self.is_mortgaged:
            return 0
            
        rent = self.rent_base
        
        # Ev ve otel kirasını hesapla
        if self.houses > 0:
            # Her ev için kira artışı (basitleştirilmiş)
            rent += self.rent_base * self.houses
        elif self.hotel:
            # Otel için kira (basitleştirilmiş)
            rent += self.rent_base * 5
            
        return rent
        
    def buy(self, player):
        """Oyuncunun mülkü satın almasını sağlar."""
        if player.pay_money(self.price):
            self.owner = player
            player.add_property(self)
            return True
        return False
        
    def mortgage(self):
        """Mülkü ipotek eder."""
        if not self.is_mortgaged and self.houses == 0 and not self.hotel:
            self.is_mortgaged = True
            return self.price / 2  # İpotek değeri genellikle mülk değerinin yarısıdır
        return 0
        
    def unmortgage(self):
        """Mülkü ipotekten çıkarır."""
        if self.is_mortgaged:
            unmortgage_cost = (self.price / 2) * 1.1  # İpotek + %10 faiz
            if self.owner.pay_money(unmortgage_cost):
                self.is_mortgaged = False
                return True
        return False
        
    def add_house(self):
        """Mülke ev ekler."""
        if self.houses < 4 and not self.is_mortgaged and not self.hotel:
            house_cost = self.price * 0.5  # Ev maliyeti (basitleştirilmiş)
            if self.owner.pay_money(house_cost):
                self.houses += 1
                return True
        return False
        
    def add_hotel(self):
        """Mülke otel ekler (4 ev olmalı)."""
        if self.houses == 4 and not self.is_mortgaged and not self.hotel:
            hotel_cost = self.price * 0.5  # Otel maliyeti (basitleştirilmiş)
            if self.owner.pay_money(hotel_cost):
                self.houses = 0
                self.hotel = True
                return True
        return False
        
    def __str__(self):
        owner_name = self.owner.name if self.owner else "Yok"
        mortgage_status = "İpotekli" if self.is_mortgaged else "İpoteksiz"
        return f"Mülk: {self.name}, Fiyat: ₺{self.price}, Kira: ₺{self.calculate_rent()}, Sahip: {owner_name}, Durum: {mortgage_status}" 