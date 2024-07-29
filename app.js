import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import ProductDetailPage from './pages/ProductDetailPage';
import { Container } from '@mui/material';

const App = () => {
  return (
    <Router>
      <Container>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/categories/:categoryname/products/:productid" element={<ProductDetailPage />} />
        </Routes>
      </Container>
    </Router>
  );
};

export default App;