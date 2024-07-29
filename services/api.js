import axios from 'axios';

// Replace with your actual backend API URL
const API_URL = 'http://localhost:5000';

export const fetchProducts = (params) => {
  return axios.get(${API_URL}/categories/${params.categoryname}/products, { params });
};

export const fetchProductDetails = (categoryname, productid) => {
  return axios.get(${API_URL}/categories/${categoryname}/products/${productid});
};