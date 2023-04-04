import React from 'react';
import './AboutPage.css';
import Arjun from './arjun.jpeg'; // Import the component for the About page
import Arnav from './arnav.jpeg'; // Import the component for the About page
import UN from './UN.png'; // Import the component for the About page


function AboutPage() {
  return (
    <div className="about-page">
      <div className="about-page-content">
        <h1 className='head'>About EcoSentinel</h1>
        <p>The idea for EcoSentinel spawned after we considered the UN’s 17 goals for sustainable development. We had noticed a lack of easy to understand and trustworthy information about the extent of ecological damage. We believe in providing reliable and unbiased information about ecological damage</p>
        <img src={UN} alt="UN Goals" className="small-image"/>

        <h1 className='head'>Methodology</h1>
       <p>The EcoSentinel pipeline begins with a continuous import of satellite imagery from Google Earth Engine. Using its API, we can deliver fresh landsat images for monitoring ecological damage. Because Google Earth Engine has its limitations with analyzing the data, we then move into Python for our Tensorflow model, analyzing segments of the Earth’s landmass for deforestation over time.</p>
<p>The data we gather on forest coverage is then fed into our time-series analysis, where we consider short and long terms trends in ecological damage to best predict how Earth’s ecological systems will grow or shrink in the future. We calculate a few key metrics:</p>
<ul>
  <li><strong>Risk:</strong> the risk of an ecosystem going beyond the point of recovery</li>
  <li><strong>Grades:</strong> an evaluation of countries (and eventually companies) on their effectiveness in reigning in ecological destruction</li>
  <li><strong>Predictive system:</strong> in the future, a system that can project the effectiveness of any legislation or other efforts based on past trends</li>
</ul>
<p>All of these findings will then be presented in digestible, yet informative, visualizations on our website.</p>
        <h2 className='head'>Our Team</h2>
        <div className="team-member">
          <img src={Arjun} alt="Team Member" className="small-image"/>
          <div className="team-member-info">
            <h3>Arjun</h3>
          </div>
        </div>
        <div className="team-member">
          <img src={Arnav} alt="Team Member" className="small-image"/>
          <div className="team-member-info">
            <h3>Arnav</h3>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AboutPage;
