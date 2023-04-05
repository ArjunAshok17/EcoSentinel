import React, { useState } from 'react';
import './NavbarHamburger.css';
import HamburgerMenu from 'react-hamburger-menu';

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const handleMenuClick = () => {
    setIsOpen(!isOpen);
  };

  const handleMenuClose = () => {
    setIsOpen(false);
  };

  return (
    <>
      <nav className="navbar">
        <div className="logo">Logo</div>
        <div className="menu">
          <HamburgerMenu
            isOpen={isOpen}
            menuClicked={handleMenuClick}
            width={30}
            height={20}
            strokeWidth={3}
            rotate={0}
            color='black'
            borderRadius={0}
            animationDuration={0.5}
          />
          <div className={`menu-content ${isOpen ? 'open' : 'close'}`} onClick={handleMenuClose}>
            <ul>
              <li><a href="#">Home</a></li>
              <li><a href="#">About</a></li>
              <li><a href="#">Services</a></li>
              <li><a href="#">Contact</a></li>
            </ul>
          </div>
        </div>
      </nav>
      <div className={`green-popup ${isOpen ? 'open' : 'close'}`} onClick={handleMenuClose}>
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Services</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </div>
    </>
  );
}

export default Navbar;
