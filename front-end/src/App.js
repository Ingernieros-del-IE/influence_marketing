import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LoginBox from './pages/login';
import AnotherPage from './pages/Main';
import Profile from './pages/Profile';
import Influ from './pages/Influencer';
import Campaign from './pages/campaign';
import SignInBox from './pages/signin';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<LoginBox />} />
        <Route exact path="/home" element={<AnotherPage />} />
        <Route exact path="/profile" element={<Profile />} />
        <Route exact path="/influencer" element={<Influ />} />
        <Route exact path="/campaign" element={<Campaign />} />
        <Route exact path="/signin" element={<SignInBox />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;