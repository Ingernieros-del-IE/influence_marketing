import React from 'react';
import SquareWithImage from './components/square';
import TopBar from './components/TopBar';
import SideBar from './components/SideBar';
import './main.css';

const handleAddToCampaign = () => {
  console.log('Add to campaign clicked');
};

const AnotherPage = () => {
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
            onAddToCampaign={handleAddToCampaign}
          />
        </div>
      );
    });
  };

  return (
    <div className="page">
      <TopBar />
      <div className="content">
        <div className="squares">{renderSquares()}</div>
        <SideBar />
      </div>
    </div>
  );
};

export default AnotherPage;