import React from 'react';
import './UserInformation.css';


const UserInformation = ({ name, category, bio, profileImage, country, hashtags, followers }) => {
  return (
    <div className="user-info">
  <img src={profileImage} alt="Profile" className="profile-image" />
  <h2 className="name">{name}</h2>
  <p className="bio">"{bio}"</p>
  <p className="email">Category: {category}</p>
  <p className="email">Country: {country}</p>
  <p className="hashtags">Hashtags: {hashtags}</p>
  <p className="followers">{followers} Followers</p>
  </div>
  );
};

export default UserInformation;