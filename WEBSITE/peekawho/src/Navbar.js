import React from 'react';
import './Navbar.css';
import Logo from './logo3.svg'

const Navbar = () => {
    return (
      <nav className="navbar">
        <div className="navbar-logo">
            <img src={Logo} alt={Logo} width="70" height="73" fill="none"/>
        </div>
        <h1 className = 'title'>Peek-a-Who!</h1>
      </nav>
    );
  };
  
  export default Navbar;