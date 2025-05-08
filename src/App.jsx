import React, { useState, useEffect } from 'react';
import GameBoard from './components/GameBoard';
import PlayerInfo from './components/PlayerInfo';
import DiceRoller from './components/DiceRoller';
import PropertyManager from './components/PropertyManager';
import './styles/App.css';

const App = () => {
  const [players, setPlayers] = useState([
    { id: 1, name: 'Oyuncu 1', money: 1500, position: 0, properties: [] },
    { id: 2, name: 'Oyuncu 2', money: 1500, position: 0, properties: [] },
  ]);
  
  const [currentPlayerIndex, setCurrentPlayerIndex] = useState(0);
  const [gameStarted, setGameStarted] = useState(false);
  const [diceValues, setDiceValues] = useState([1, 1]);
  const [propertyModalVisible, setPropertyModalVisible] = useState(false);
  const [currentProperty, setCurrentProperty] = useState(null);

  const startGame = () => {
    setGameStarted(true);
  };

  const rollDice = () => {
    const dice1 = Math.floor(Math.random() * 6) + 1;
    const dice2 = Math.floor(Math.random() * 6) + 1;
    setDiceValues([dice1, dice2]);
    
    const currentPlayer = players[currentPlayerIndex];
    const steps = dice1 + dice2;
    const newPosition = (currentPlayer.position + steps) % 40; // 40 kare olduğunu varsayalım
    
    // Oyuncunun pozisyonunu güncelle
    const updatedPlayers = [...players];
    updatedPlayers[currentPlayerIndex] = {
      ...currentPlayer,
      position: newPosition
    };
    setPlayers(updatedPlayers);
    
    // Başlangıç noktasından geçildiyse para ver
    if (newPosition < currentPlayer.position) {
      givePassStartMoney(currentPlayerIndex);
    }
    
    // Gelinen karenin etkilerini kontrol et
    checkSquareEffect(newPosition);
  };

  const givePassStartMoney = (playerIndex) => {
    const updatedPlayers = [...players];
    updatedPlayers[playerIndex] = {
      ...updatedPlayers[playerIndex],
      money: updatedPlayers[playerIndex].money + 200
    };
    setPlayers(updatedPlayers);
  };

  const checkSquareEffect = (position) => {
    // Her pozisyonda farklı etki olacak
    const properties = [
      { id: 1, position: 1, name: 'Sultanahmet', price: 60, rent: 2, owner: null, color: 'brown' },
      { id: 2, position: 3, name: 'Karaköy', price: 60, rent: 4, owner: null, color: 'brown' },
      // diğer mülkler...
    ];
    
    const property = properties.find(p => p.position === position);
    
    if (property) {
      // Mülk karesine gelindi
      setCurrentProperty(property);
      setPropertyModalVisible(true);
    }
    
    // Diğer özel kareler (şans, vergi vs) burada kontrol edilebilir
  };

  const buyProperty = () => {
    if (!currentProperty) return;
    
    const currentPlayer = players[currentPlayerIndex];
    
    // Oyuncunun parası yeterli mi kontrol et
    if (currentPlayer.money >= currentProperty.price) {
      const updatedPlayers = [...players];
      
      // Parayı düş
      updatedPlayers[currentPlayerIndex] = {
        ...currentPlayer,
        money: currentPlayer.money - currentProperty.price,
        properties: [...currentPlayer.properties, currentProperty.id]
      };
      
      setPlayers(updatedPlayers);
      setPropertyModalVisible(false);
      
      // Sırayı diğer oyuncuya geçir
      nextTurn();
    }
  };

  const nextTurn = () => {
    setCurrentPlayerIndex((currentPlayerIndex + 1) % players.length);
  };

  return (
    <div className="app">
      <h1>Emlak Oyunu</h1>
      
      {!gameStarted ? (
        <div className="start-game">
          <button onClick={startGame}>Oyunu Başlat</button>
        </div>
      ) : (
        <div className="game-container">
          <div className="game-info">
            <PlayerInfo 
              players={players} 
              currentPlayerIndex={currentPlayerIndex} 
            />
            <DiceRoller 
              diceValues={diceValues}
              onRoll={rollDice} 
            />
          </div>
          
          <GameBoard 
            players={players}
          />
          
          {propertyModalVisible && currentProperty && (
            <PropertyManager 
              property={currentProperty}
              player={players[currentPlayerIndex]}
              onBuy={buyProperty}
              onCancel={() => {
                setPropertyModalVisible(false);
                nextTurn();
              }}
            />
          )}
        </div>
      )}
    </div>
  );
};

export default App; 