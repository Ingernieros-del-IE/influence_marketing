import React from 'react';
import LoginBox from './components/login_box';
import Logo from './components/logo';
import './log.css';

function App() {
  return (
    <div>
      <div className='logo'><Logo /></div>
      <LoginBox />
    </div>
  );
}

export default App;