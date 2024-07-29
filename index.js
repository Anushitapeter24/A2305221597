import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { CssBaseline } from '@mui/material';

// Set up the root element
const root = ReactDOM.createRoot(document.getElementById('root'));

// Render the App component with baseline CSS
root.render(
  <React.StrictMode>
    <CssBaseline />
    <App />
  </React.StrictMode>
);