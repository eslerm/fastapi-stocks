import React from 'react';
import { render, screen } from '@testing-library/react';
import Footer from './Footer';

test('renders Mark Esler', () => {
  render(<Footer />);
  const linkElement = screen.getByText(/Mark Esler/i);
  expect(linkElement).toBeInTheDocument();
});
