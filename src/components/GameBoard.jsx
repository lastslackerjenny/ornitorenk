import React from 'react';
import '../styles/GameBoard.css';

const boardSquares = [
  { id: 0, type: 'start', name: 'BAŞLA' },
  { id: 1, type: 'property', name: 'Sultanahmet', price: 60, color: 'brown' },
  { id: 2, type: 'chest', name: 'Kamu Fonu' },
  { id: 3, type: 'property', name: 'Karaköy', price: 60, color: 'brown' },
  { id: 4, type: 'tax', name: 'Gelir Vergisi', amount: 200 },
  { id: 5, type: 'railroad', name: 'Haydarpaşa Garı', price: 200 },
  { id: 6, type: 'property', name: 'Beşiktaş', price: 100, color: 'lightblue' },
  { id: 7, type: 'chance', name: 'Şans' },
  { id: 8, type: 'property', name: 'Taksim', price: 100, color: 'lightblue' },
  { id: 9, type: 'property', name: 'Harbiye', price: 120, color: 'lightblue' },
  { id: 10, type: 'jail', name: 'Hapishane (Ziyaretçi)' },
  { id: 11, type: 'property', name: 'Şişli', price: 140, color: 'pink' },
  { id: 12, type: 'utility', name: 'Elektrik İdaresi', price: 150 },
  { id: 13, type: 'property', name: 'Mecidiyeköy', price: 140, color: 'pink' },
  { id: 14, type: 'property', name: 'Bostancı', price: 160, color: 'pink' },
  { id: 15, type: 'railroad', name: 'Sirkeci Garı', price: 200 },
  { id: 16, type: 'property', name: 'Erenköy', price: 180, color: 'orange' },
  { id: 17, type: 'chest', name: 'Kamu Fonu' },
  { id: 18, type: 'property', name: 'Caddebostan', price: 180, color: 'orange' },
  { id: 19, type: 'property', name: 'Nişantaşı', price: 200, color: 'orange' },
  { id: 20, type: 'parking', name: 'Serbest Park' },
  { id: 21, type: 'property', name: 'Teşvikiye', price: 220, color: 'red' },
  { id: 22, type: 'chance', name: 'Şans' },
  { id: 23, type: 'property', name: 'Maçka', price: 220, color: 'red' },
  { id: 24, type: 'property', name: 'Bebek', price: 240, color: 'red' },
  { id: 25, type: 'railroad', name: 'Ankara Garı', price: 200 },
  { id: 26, type: 'property', name: 'Yeşilköy', price: 260, color: 'yellow' },
  { id: 27, type: 'property', name: 'Levent', price: 260, color: 'yellow' },
  { id: 28, type: 'utility', name: 'Sular İdaresi', price: 150 },
  { id: 29, type: 'property', name: 'Etiler', price: 280, color: 'yellow' },
  { id: 30, type: 'gotojail', name: 'Hapse Git' },
  { id: 31, type: 'property', name: 'Fenerbahçe', price: 300, color: 'green' },
  { id: 32, type: 'property', name: 'Bağdat Caddesi', price: 300, color: 'green' },
  { id: 33, type: 'chest', name: 'Kamu Fonu' },
  { id: 34, type: 'property', name: 'Nişantaşı', price: 320, color: 'green' },
  { id: 35, type: 'railroad', name: 'İzmir Garı', price: 200 },
  { id: 36, type: 'chance', name: 'Şans' },
  { id: 37, type: 'property', name: 'Tarabya', price: 350, color: 'blue' },
  { id: 38, type: 'tax', name: 'Lüks Vergisi', amount: 100 },
  { id: 39, type: 'property', name: 'Yeniköy', price: 400, color: 'blue' },
];

const GameBoard = ({ players }) => {
  return (
    <div className="game-board">
      {boardSquares.map((square) => (
        <div 
          key={square.id} 
          className={`board-square square-${square.id} square-type-${square.type}`}
          style={{ 
            borderTop: square.color ? `4px solid ${square.color}` : 'none'
          }}
        >
          <div className="square-content">
            <div className="square-name">{square.name}</div>
            {square.price && <div className="square-price">{square.price}₺</div>}
            {square.amount && <div className="square-amount">Öde: {square.amount}₺</div>}
          </div>
          
          <div className="player-tokens">
            {players.map(player => (
              player.position === square.id && (
                <div key={player.id} className={`player-token player-${player.id}`}>
                  {player.id}
                </div>
              )
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default GameBoard; 