import React, { useState } from 'react';
import './HomePage.css';
import Map from './Map.js';
import githubLogo from './github-logo.png'; // Import the image file for the GitHub logo
import slidesLogo from './slides-icon.png'; // Import the image file for the Slides logo
import ecoSentinelLogo from './ecosentinel-logo.png'; // Import the image file for the EcoSentinel logo
import AboutPage from './AboutPage.js'; // Import the component for the About page

function HomePage() {
  const [activeButton, setActiveButton] = useState('page1');
  const [showAboutPage, setShowAboutPage] = useState(false);

  return (
    <div>
      <div className="section1">
        <div className="left">
            <h1> EcoSentinel </h1>
        </div>
        <div className="center">
            <img src={ecoSentinelLogo} alt="Logo" className="ecosentinel-logo"/>
        </div>
        <div className="right">
          <button
            className={activeButton === 'page1' ? 'active' : ''}
            onClick={() => {
              setActiveButton('page1');
              setShowAboutPage(false);
              window.location.href = '/page1';
            }}
          >
            The Pipeline
          </button>
          <button
            className={activeButton === 'page2' ? 'active' : ''}
            onClick={() => {
              setActiveButton('page2');
              setShowAboutPage(true);
            }}
          >
            About
          </button>
          <button>
          <a href="https://github.com/ArjunAshok17/EcoSentinel" target="_blank" className="github-button">
            <img src={githubLogo} alt="Github Logo" className="github-logo" />
            <span>GitHub</span>
          </a>
          </button>
          <button>
          <a href="https://docs.google.com/presentation/d/1Dyc2Kgvr4RBW4HqUauppe-iLxGonAkIIDn5oYIght_U/edit?usp=sharing" target="_blank" className="slides-button">
            <img src={slidesLogo} alt="Google Slides Logo" className="slides-logo" />
            <span>Slides</span>
          </a>
          </button>
        </div>
      </div>
      <div className="section2">
      <h2>Information about ecological damage that is <b style={{ color: 'black' }}>reliable, unbiased and trustworthy</b></h2>
      </div>
      <div className="section3">
        {showAboutPage ? <AboutPage /> : <Map />}
      </div>
    </div>
  );
}

export default HomePage;



