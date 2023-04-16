import React from 'react';
import SigninBox from './components/signin_box';
import Logo from './components/logo';
import './log.css';

function SignInBox() {
  return (
    <div>
      <div className='logo'><Logo /></div>
      <SigninBox />
    </div>
  );
}

export default SignInBox;