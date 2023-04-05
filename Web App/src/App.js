import React, { useState, useEffect } from 'react';
import HomePage from './HomePage';
import './App.css'; // import your CSS file here

function LoadingScreen({ progress }) {
  return (
    <div className="loading-screen">
      <div className="loading-circle">
        <div className="progress" style={{ transform: `rotate(${progress * 3.6}deg)` }}></div>
        <div className="progress-text">{Math.round(progress)}%</div>
      </div>
    </div>
  );
}

function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    // Simulate loading time for demonstration purposes
    let intervalId = setInterval(() => {
      setProgress((progress) => {
        if (progress >= 100) {
          clearInterval(intervalId);
          setIsLoading(false);
          return 100;
        }
        return progress + 1;
      });
    }, 25);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return (
    <div className="App">
      {isLoading ? (
        <LoadingScreen progress={progress} />
      ) : (
        <HomePage />
      )}
    </div>
  );
}

export default App;




