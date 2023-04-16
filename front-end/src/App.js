import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LoginBox from './pages/login';
import AnotherPage from './pages/AnotherPage';
import Profile from './pages/Profile';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<LoginBox />} />
        <Route exact path="/home" element={<AnotherPage />} />
        <Route exact path="/profile" element={<Profile />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;