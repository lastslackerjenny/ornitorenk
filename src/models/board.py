import random
from .property import Property

class Board:
    def __init__(self):
        self.squares = []
        self.chance_cards = []
        self.community_chest_cards = []
        self.initialize_board()
        
    def initialize_board(self):
        """Oyun tahtasını başlatır ve kareleri oluşturur."""
        # Örnek mülkler (basitleştirilmiş)
        self.squares = [
            {"type": "go", "name": "Başlangıç", "position": 0},
            {"type": "property", "obj": Property("Karaköy", 60, 2, "kahverengi", 1)},
            {"type": "community_chest", "name": "Kamu Fonu", "position": 2},
            {"type": "property", "obj": Property("Sultanahmet", 60, 4, "kahverengi", 3)},
            {"type": "tax", "name": "Gelir Vergisi", "amount": 200, "position": 4},
            {"type": "railroad", "name": "Haydarpaşa Garı", "price": 200, "position": 5},
            {"type": "property", "obj": Property("Beşiktaş", 100, 6, "açık mavi", 6)},
            {"type": "chance", "name": "Şans", "position": 7},
            {"type": "property", "obj": Property("Taksim", 100, 6, "açık mavi", 8)},
            {"type": "property", "obj": Property("Harbiye", 120, 8, "açık mavi", 9)},
            {"type": "jail", "name": "Kodes / Ziyaret", "position": 10},
            # ... tahta kareleri devam edecek (toplam 40 kare)
        ]
        
        # Şans kartları
        self.chance_cards = [
            {"type": "move", "destination": 0, "description": "Başlangıç noktasına ilerle."},
            {"type": "move", "destination": 10, "description": "Kodese git. Başlangıç noktasından geçersen 200₺ alamazsın."},
            {"type": "money", "amount": 50, "description": "Banka sana 50₺ ödüyor."},
            # ... diğer şans kartları
        ]
        
        # Kamu Fonu kartları
        self.community_chest_cards = [
            {"type": "money", "amount": 100, "description": "Miras kaldı! 100₺ al."},
            {"type": "money", "amount": -50, "description": "Doktor ücreti öde. 50₺ ver."},
            {"type": "get_out_of_jail", "description": "Kodesten bedava çıkış kartı."},
            # ... diğer kamu fonu kartları
        ]
        
        # Kartları karıştır
        random.shuffle(self.chance_cards)
        random.shuffle(self.community_chest_cards)
    
    def roll_dice(self):
        """İki zar atar ve toplamını döndürür."""
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1, dice2, dice1 + dice2
    
    def get_square(self, position):
        """Belirli bir pozisyondaki kareyi döndürür."""
        for square in self.squares:
            if "position" in square and square["position"] == position:
                return square
        return None
    
    def draw_chance_card(self):
        """Bir şans kartı çeker."""
        card = self.chance_cards.pop(0)
        self.chance_cards.append(card)  # Kartı desteye geri koy
        return card
    
    def draw_community_chest_card(self):
        """Bir kamu fonu kartı çeker."""
        card = self.community_chest_cards.pop(0)
        self.community_chest_cards.append(card)  # Kartı desteye geri koy
        return card