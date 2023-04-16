import React, { useState } from 'react';
import { BrowserRouter, Route, Link } from "react-router-dom";
import './login.css';


function SigninBox() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Username: ${username}, Password: ${password}`);
  };

  const buttonStyle = {
    backgroundColor: '#f37930',
    border: 'none',
    borderRadius: '4px',
    color: '#ffffff',
    padding: '8px 16px',
    textDecoration: 'none',
  };

  return (
    <div className="login-box">
      <h2>SignIn</h2>
      <p></p>
      <p></p>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="username">Instagram Username:</label>
          <input
            type="text"
            id="username"
            name="username"
            value={username}
            onChange={handleUsernameChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="username">Country:</label>
          <input
            type="text"
            id="username"
            name="username"
            value={username}
            onChange={handleUsernameChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Create Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={password}
            onChange={handlePasswordChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Repeat Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={password}
            onChange={handlePasswordChange}
          />
        </div>
        <div className='login-button'>
        <Link to="/home" style={buttonStyle} button>
          SignIn
        </Link>
        </div>
      </form>
    </div>
  );
}

export default SigninBox;