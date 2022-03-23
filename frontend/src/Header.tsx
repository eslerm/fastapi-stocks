import React from 'react';
import logo from './logo.svg';
import './Header.css';

function Header() {
  return (
    <header>
      <a href="/">
        <h1>Oil Price Day</h1>
        <img src={logo} className="logo" alt="logo"/>
      </a>
      <h2>Daily Oil Prices</h2>
    </header>
  );
}

export default Header;
