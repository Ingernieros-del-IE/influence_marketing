import React from 'react';
import './square.css';
import { BrowserRouter, Route, Link } from "react-router-dom";

const AddToCampaignButton = ({ onClick }) => {
  const handleClick = () => {
    onClick();
    alert("Added to your campaign.");
  };

  return (
    <button className="add-to-campaign-button" onClick={handleClick}>
      Add to Campaign
    </button>
  );
};

const SquareWithImage = ({ imageUrl, name, text1, text2, onAddToCampaign }) => {
  return (
    <div className="square">
      <img src={imageUrl} className="circle" />
      <div className="name">
      <Link to="/influencer">
        <h2 className="name">{name}</h2></Link>
      </div>
      <p className="text">{text1} ENGRATE</p>
      <p className="text">{text2} CATEGORY</p>
      <AddToCampaignButton onClick={onAddToCampaign} />
    </div>
  );
};

export default SquareWithImage;