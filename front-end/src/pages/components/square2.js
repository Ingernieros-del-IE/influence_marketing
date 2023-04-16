import React from 'react';
import './square.css';
import { BrowserRouter, Route, Link } from "react-router-dom";

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
      <div className="name">
      <Link to="/influencer">
        <h2 className="name">{name}</h2></Link>
      </div>
      <p className="text">{text1} ENGRATE</p>
      <p className="text">{text2} CATEGORY</p>
      <h4 className="added">Added to Campaign</h4>
    </div>
  );
};

export default SquareWithImage;