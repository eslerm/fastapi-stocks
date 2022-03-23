import React from 'react';
import { render, screen } from '@testing-library/react';
import Header from './Header';

test('renders Daily Oil Prices', () => {
  render(<Header />);
  const linkElement = screen.getByText(/Daily Oil Prices/i);
  expect(linkElement).toBeInTheDocument();
});
