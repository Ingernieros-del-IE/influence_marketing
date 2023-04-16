import React from 'react';
import InfluInformation from './components/InfluInformation';
import TopBar from './components/TopBar';

const name = "@username";
const bio = "Vida. Viajes. Familia. Perfumes.";
const profileImage = "https://via.placeholder.com/150";
const category = "Beauty";
const country = "Spain";
const hashtags = "#papa #colonia #perfume";
const followers = "123,987";
const engrate = "0.09";

function Influ() {
  return (
    <div>
      <TopBar />
      <InfluInformation name={name} bio={bio} profileImage={profileImage} category={category} country={country} hashtags={hashtags} followers={followers} engrate={engrate}/>
    </div>
  );
}

export default Influ;