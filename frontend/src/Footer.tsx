import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer>
      <p>
        Powered by <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer">FastAPI</a>, <a href="https://reactjs.org/" target="_blank" rel="noreferrer">React.js</a>, <a href="https://d3js.org/" target="_blank" rel="noreferrer">D3.js</a> and <a href="https://aws.amazon.com/" target="_blank" rel="noreferrer">AWS</a><br />
        Built, operated, and designed by <a href="https://markesler.com" title="Mark Esler">Mark Esler</a>
      </p>
    </footer>
  );
}

export default Footer;
