import React, { useState } from 'react';
import { BrowserRouter, Route, Link } from "react-router-dom";
import './login.css';


function LoginBox() {
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
      <h2>Login</h2>
      <p></p>
      <p></p>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            name="username"
            value={username}
            onChange={handleUsernameChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
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
          LogIn
        </Link>
        </div>
      </form>
    </div>
  );
}

export default LoginBox;