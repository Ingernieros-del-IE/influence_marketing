import React from 'react';
import logo from '../assets/logo.png';
import './TopBar.css';
import { BrowserRouter, Route, Link } from "react-router-dom";

const TopBar = () => {
  return (
    <div className="top-bar">
      <Link to="/home"><img src={logo} alt="Logo" className="logo" /></Link>
      <div className="search-bar">
        <input type="text" placeholder="Search" />
      </div>
      <div className="name">
      <Link to="/profile"><button className="button">
          @perfumeriasavenida
        </button></Link>
      </div>
      <div className="name">
      <Link to="/campaign"><button className="button">
          View Campaign
        </button></Link>
      </div>
    </div>
  );
};

export default TopBar;