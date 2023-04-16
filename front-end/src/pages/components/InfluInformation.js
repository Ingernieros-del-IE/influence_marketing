import React from 'react';
import './InfluInformation.css';


const InfluInformation = ({ name, category, bio, profileImage, country, hashtags, followers, engrate }) => {
  return (
    <div className="user-info">
  <img src={profileImage} alt="Profile" className="profile-image" />
  <h2 className="name">{name}</h2>
  <p className="bio">"{bio}"</p>
  <p className="email">Category: {category}</p>
  <p className="email">Engagement Rate: {engrate}</p>
  <p className="email">Country: {country}</p>
  <p className="hashtags">Hashtags: {hashtags}</p>
  <p className="followers">{followers} Followers</p>
  </div>
  );
};

export default InfluInformation;