import React from 'react';
import '../styles/PropertyManager.css';

const PropertyManager = ({ property, player, onBuy, onCancel }) => {
  const canBuy = player.money >= property.price;

  return (
    <div className="property-modal">
      <div className="property-card">
        <div className="property-header" style={{ backgroundColor: property.color }}>
          <h3>{property.name}</h3>
        </div>
        
        <div className="property-details">
          <p>Satın alma bedeli: <strong>{property.price}₺</strong></p>
          <p>Kira bedeli: <strong>{property.rent}₺</strong></p>
          
          {property.owner ? (
            <div className="property-owner">
              <p>Sahibi: Oyuncu {property.owner}</p>
              <p>Ödemeniz gereken kira: {property.rent}₺</p>
            </div>
          ) : (
            <div className="property-purchase">
              <p>Bu mülk satın alınabilir</p>
              <p>Mevcut paranız: {player.money}₺</p>
              
              {canBuy ? (
                <div className="action-buttons">
                  <button className="buy-button" onClick={onBuy}>Satın Al</button>
                  <button className="cancel-button" onClick={onCancel}>Vazgeç</button>
                </div>
              ) : (
                <div className="insufficient-funds">
                  <p>Yeterli paranız yok!</p>
                  <button className="cancel-button" onClick={onCancel}>Tamam</button>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default PropertyManager; 