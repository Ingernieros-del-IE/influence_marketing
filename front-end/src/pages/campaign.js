import React from 'react';
import SquareWithImage from './components/square2';
import TopBar from './components/TopBar';
import './campaign.css';
import './components/campaignTitle.css';

const Campaign = () => {
  const squares = [
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
    {
      imageUrl: 'https://via.placeholder.com/150',
      name: 'Username',
      text1: '0.09',
      text2: 'Lifestyle'
    },
  ];

  const renderSquares = () => {
    return squares.map((square, index) => {
      return (
        <div className="square-container" key={index}>
          <SquareWithImage
            imageUrl={square.imageUrl}
            name={square.name}
            text1={square.text1}
            text2={square.text2}
            onAddToCampaign={() => console.log('Add to campaign clicked')}
          />
        </div>
      );
    });
  };

  return (
    <div className="page">
      <TopBar />
      <div className="title-box">
        <h1 className="title">"Christmas Campaign"</h1>
        <div className="subtitle">
          <span className="brand">Perfumerías Avenida</span>
          <span className="cost">15,035.65€</span>
        </div>
      </div>
      <div className="content">
        <div className="squares2">{renderSquares()}</div>
      </div>
    </div>
  );
};

export default Campaign;