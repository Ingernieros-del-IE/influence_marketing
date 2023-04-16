import React from 'react';
import './square.css';

const AddToCampaignButton = ({ onClick }) => {
  return (
    <button className="add-to-campaign-button" onClick={onClick}>
      Add to Campaign
    </button>
  );
};

const SquareWithImage = ({ imageUrl, name, text1, text2, onAddToCampaign }) => {
  return (
    <div className="square">
      <img src={imageUrl} className="circle" />
      <h2 className="name">{name}</h2>
      <p className="text">{text1} ENGRATE</p>
      <p className="text">{text2} CATEGORY</p>
      <AddToCampaignButton onClick={onAddToCampaign} />
    </div>
  );
};

export default SquareWithImage;