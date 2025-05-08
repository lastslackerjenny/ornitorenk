from src.game import MonopolyGame

def main():
    """Ana program giriş noktası."""
    print("Monopoly Oyununa Hoş Geldiniz!")
    
    # Oyuncu sayısını al
    while True:
        try:
            player_count = int(input("Kaç oyuncu oynayacak? (2-4): "))
            if 2 <= player_count <= 4:
                break
            else:
                print("Lütfen 2 ile 4 arasında bir sayı girin.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
    
    # Oyuncu isimlerini al
    player_names = []
    for i in range(player_count):
        name = input(f"{i+1}. oyuncunun adını girin: ")
        player_names.append(name)
    
    # Tur sayısını al
    while True:
        try:
            max_turns = int(input("Maksimum kaç tur oynamak istersiniz? (Önerilen: 20-100): "))
            if max_turns > 0:
                break
            else:
                print("Lütfen pozitif bir sayı girin.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
    
    # Oyunu başlat
    game = MonopolyGame(player_names)
    game.play_game(max_turns)
    
    print("\nOyun sona erdi. Tekrar oynamak için programı yeniden başlatın.")

if __name__ == "__main__":
    main() 