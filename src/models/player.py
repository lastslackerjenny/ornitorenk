class Player:
    def __init__(self, name, money=1500):
        self.name = name
        self.money = money
        self.position = 0  # Başlangıç noktasında (GO)
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0
        self.get_out_of_jail_free_cards = 0
        
    def move(self, steps):
        """Oyuncuyu belirtilen adım kadar ilerletir."""
        old_position = self.position
        self.position = (self.position + steps) % 40  # 40 kare standart Monopoly tahtası
        # Başlangıç noktasından geçti mi kontrol et
        if self.position < old_position:
            return True  # Başlangıç noktasından geçti
        return False
        
    def add_money(self, amount):
        """Oyuncuya para ekler."""
        self.money += amount
        
    def pay_money(self, amount):
        """Oyuncunun para ödemesini sağlar."""
        if self.money >= amount:
            self.money -= amount
            return True
        return False
        
    def add_property(self, property):
        """Oyuncuya mülk ekler."""
        self.properties.append(property)
        
    def remove_property(self, property):
        """Oyuncudan mülk çıkarır."""
        if property in self.properties:
            self.properties.remove(property)
            return True
        return False
    
    def go_to_jail(self):
        """Oyuncuyu kodese gönderir."""
        self.in_jail = True
        self.position = 10  # 10. kare genellikle kodestir
        self.jail_turns = 0
        
    def get_out_of_jail(self):
        """Oyuncuyu kodesten çıkarır."""
        self.in_jail = False
        
    def __str__(self):
        return f"Oyuncu: {self.name}, Para: ₺{self.money}, Pozisyon: {self.position}" 