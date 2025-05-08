import React from 'react';
import '../styles/DiceRoller.css';

const DiceRoller = ({ diceValues, onRoll }) => {
  return (
    <div className="dice-roller">
      <h2>Zar At</h2>
      
      <div className="dice-container">
        <div className={`dice dice-${diceValues[0]}`}>
          {Array.from({ length: diceValues[0] }).map((_, i) => (
            <div key={i} className="dice-dot"></div>
          ))}
        </div>
        
        <div className={`dice dice-${diceValues[1]}`}>
          {Array.from({ length: diceValues[1] }).map((_, i) => (
            <div key={i} className="dice-dot"></div>
          ))}
        </div>
      </div>
      
      <div className="dice-total">
        Toplam: {diceValues[0] + diceValues[1]}
      </div>
      
      <button className="roll-button" onClick={onRoll}>
        Zar At
      </button>
    </div>
  );
};

export default DiceRoller; 