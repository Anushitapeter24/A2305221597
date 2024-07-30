import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Container, Typography, Card, CardContent, CardMedia } from '@mui/material';
import { fetchProductDetails } from '../services/api';

const ProductDetail = () => {
  const { categoryname, productid } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetchProductDetails(categoryname, productid).then(response => {
      setProduct(response.data);
    });
  }, [categoryname, productid]);

  if (!product) return <div>Loading...</div>;

  return (
    <Container>
      <Card>
        <CardMedia
          component="img"
          height="140"
          image={https://source.unsplash.com/random/400x300?sig=${product.unique_id}}
          alt={product.name}
        />
        <CardContent>
          <Typography variant="h4">{product.name}</Typography>
          <Typography color="textSecondary">{product.company}</Typography>
          <Typography variant="body1">Category: {product.category}</Typography>
          <Typography variant="body1">Price: ${product.price}</Typography>
          <Typography variant="body1">Rating: {product.rating}</Typography>
          <Typography variant="body1">Discount: {product.discount}%</Typography>
          <Typography variant="body1">Availability: {product.availability ? 'In Stock' : 'Out of Stock'}</Typography>
        </CardContent>
      </Card>
    </Container>
  );
};

export default ProductDetail;