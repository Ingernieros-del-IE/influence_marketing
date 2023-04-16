import React from 'react';
import UserInformation from './components/UserInformation';
import TopBar from './components/TopBar';

const name = "@perfumeriasavenida";
const bio = "Ponte guapo pa ligar";
const profileImage = "https://via.placeholder.com/150";
const category = "Beauty";
const country = "Spain";
const hashtags = "#perfume #colonia #ponteguapa";
const followers = "23,987";

function Profile() {
  return (
    <div>
      <TopBar />
      <UserInformation name={name} bio={bio} profileImage={profileImage} category={category} country={country} hashtags={hashtags} followers={followers}/>
    </div>
  );
}

export default Profile;