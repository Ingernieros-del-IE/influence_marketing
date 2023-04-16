import React from 'react';
import RangeSlider from './rangebar';
import './sidebar.css';

const SideBar = () => {
  return (
    <div className="sidebar">
      <h2>Search by Keywords</h2>
      <div className="search-container">
        <input type="text" placeholder="Enter keywords" />
        <button>Search</button>
      </div>
      <div className="range-container">
        <RangeSlider />
      </div>
      <h2>Search by Location</h2>
      <div className="search-container">
        <input type="text" placeholder="Enter location" />
        <button>Search</button>
      </div>
      <h2></h2>
      <div className="sidep"><p>For more accurate results, please contact us.</p></div>
      <h2></h2>
      <h2>Contact</h2>
      <div className="sidep"><p>ingenierosdelie@ie.edu</p></div>
      <div className="sidep"><p>P.º de la Castellana, 259, 28029 Madrid</p></div>
      <h2></h2>
      <div className="sidep"><p>©2023. Ingenieros De lIE</p></div>
    </div>
  );
};

export default SideBar;
