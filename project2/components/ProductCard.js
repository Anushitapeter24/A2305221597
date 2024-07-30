import React from 'react';
import { Card, CardContent, Typography, CardMedia } from '@mui/material';

const ProductCard = ({ product }) => {
  return (
    <Card>
      <CardMedia
        component="img"
        height="140"
        image={https://source.unsplash.com/random/400x300?sig=${product.unique_id}}
        alt={product.name}
      />
      <CardContent>
        <Typography variant="h5">{product.name}</Typography>
        <Typography color="textSecondary">{product.company}</Typography>
        <Typography variant="body2" color="textSecondary">Category: {product.category}</Typography>
        <Typography variant="body2" color="textSecondary">Price: ${product.price}</Typography>
        <Typography variant="body2" color="textSecondary">Rating: {product.rating}</Typography>
        <Typography variant="body2" color="textSecondary">Discount: {product.discount}%</Typography>
        <Typography variant="body2" color="textSecondary">Availability: {product.availability ? 'In Stock' : 'Out of Stock'}</Typography>
      </CardContent>
    </Card>
  );
};

export default ProductCard;