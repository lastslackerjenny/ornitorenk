from models.player import Player
from models.board import Board

class MonopolyGame:
    def __init__(self, player_names):
        self.board = Board()
        self.players = [Player(name) for name in player_names]
        self.current_player_index = 0
        self.doubles_count = 0
        self.game_over = False
        self.winner = None
        
    def get_current_player(self):
        """Mevcut oyuncuyu döndürür."""
        return self.players[self.current_player_index]
        
    def next_player(self):
        """Sırayı sonraki oyuncuya geçirir."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.doubles_count = 0
        
    def play_turn(self):
        """Bir oyuncu turu oynatır."""
        player = self.get_current_player()
        
        # Eğer oyuncu kodesteyse
        if player.in_jail:
            # Kodesten çıkma mantığı gelecek
            player.jail_turns += 1
            if player.jail_turns >= 3:
                player.get_out_of_jail()
            else:
                # Oyuncu para ödeyerek veya zar atarak çıkabilir
                pass
            
            # Hala kodesteyse sonraki oyuncuya geç
            if player.in_jail:
                self.next_player()
                return
        
        # Zar at
        dice1, dice2, total = self.board.roll_dice()
        doubles = (dice1 == dice2)
        
        # Çift zar kontrolü
        if doubles:
            self.doubles_count += 1
            if self.doubles_count == 3:
                print(f"{player.name} üç kez çift zar attı! Kodese gidiyor!")
                player.go_to_jail()
                self.next_player()
                return
        else:
            self.doubles_count = 0
        
        # Oyuncuyu hareket ettir
        passed_go = player.move(total)
        if passed_go:
            player.add_money(200)
            print(f"{player.name} Başlangıç noktasından geçti ve 200₺ kazandı!")
        
        position = player.position
        square = self.board.get_square(position)
        
        if square:
            # Kare türüne göre işlem yap
            if square["type"] == "property":
                property_obj = square["obj"]
                if property_obj.owner is None:
                    # Satın alma mantığı gelecek
                    pass
                elif property_obj.owner != player:
                    # Kira ödeme mantığı gelecek
                    rent = property_obj.calculate_rent()
                    print(f"{player.name}, {property_obj.owner.name}'a {rent}₺ kira ödüyor!")
                    player.pay_money(rent)
                    property_obj.owner.add_money(rent)
            
            elif square["type"] == "chance":
                card = self.board.draw_chance_card()
                print(f"Şans kartı: {card['description']}")
                # Kart işlemleri gelecek
            
            elif square["type"] == "community_chest":
                card = self.board.draw_community_chest_card()
                print(f"Kamu Fonu kartı: {card['description']}")
                # Kart işlemleri gelecek
            
            elif square["type"] == "tax":
                tax_amount = square["amount"]
                print(f"{player.name}, {tax_amount}₺ vergi ödüyor!")
                player.pay_money(tax_amount)
                
            elif square["type"] == "jail":
                print(f"{player.name} kodesi ziyaret ediyor.")
                
            elif square["type"] == "go_to_jail":
                print(f"{player.name} kodese gidiyor!")
                player.go_to_jail()
        
        # Oyuncunun iflasını kontrol et
        if player.money < 0:
            self.handle_bankruptcy(player)
        
        # Çift zar atılmışsa tekrar oyna, değilse sıradaki oyuncuya geç
        if not doubles and not player.in_jail:
            self.next_player()
        
    def handle_bankruptcy(self, player):
        """Oyuncunun iflası durumunda yapılacak işlemler."""
        print(f"{player.name} iflas etti!")
        
        # Mülkleri serbest bırak
        for prop in player.properties:
            prop.owner = None
        
        # Oyuncuyu oyundan çıkar
        self.players.remove(player)
        
        # Oyun sonunu kontrol et
        if len(self.players) == 1:
            self.game_over = True
            self.winner = self.players[0]
            print(f"Oyun bitti! Kazanan: {self.winner.name}")
        
        # Sıradaki oyuncuyu düzelt
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0
            
    def play_game(self, max_turns=100):
        """Oyunu belirli tur sayısına kadar oynat."""
        turn_count = 0
        
        while not self.game_over and turn_count < max_turns:
            print(f"\nTur {turn_count + 1} - Sıradaki oyuncu: {self.get_current_player().name}")
            self.play_turn()
            turn_count += 1
            
        if not self.game_over:
            print("\nMaksimum tur sayısına ulaşıldı!")
            # En zengin oyuncuyu belirle
            richest_player = max(self.players, key=lambda p: p.money)
            print(f"En zengin oyuncu: {richest_player.name} ({richest_player.money}₺)")
            
# Test - Eğer bu dosya direkt çalıştırılırsa
if __name__ == "__main__":
    game = MonopolyGame(["Ahmet", "Mehmet", "Ayşe", "Fatma"])
    game.play_game(20)  # 20 tur oyna