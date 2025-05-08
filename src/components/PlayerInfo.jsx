import React from 'react';
import '../styles/PlayerInfo.css';

const PlayerInfo = ({ players, currentPlayerIndex }) => {
  return (
    <div className="player-info">
      <h2>Oyuncular</h2>
      
      <div className="players-list">
        {players.map((player, index) => (
          <div 
            key={player.id} 
            className={`player-card ${index === currentPlayerIndex ? 'active-player' : ''}`}
          >
            <div className="player-name">{player.name}</div>
            <div className="player-money">{player.money}₺</div>
            <div className="player-properties">
              <h4>Mülkler ({player.properties.length})</h4>
              {player.properties.length > 0 ? (
                <ul>
                  {player.properties.map(propId => (
                    <li key={propId}>Mülk #{propId}</li>
                  ))}
                </ul>
              ) : (
                <p>Henüz mülk yok</p>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PlayerInfo; 