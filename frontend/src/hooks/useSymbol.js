import { useState, useEffect } from 'react';
import { fetch } from './fetch';

export function useSymbol(symbol) {

  const [history, setHistory] = useState();

  useEffect(async () => {
    const result = await fetch('/history/' + symbol);
    console.log(symbol);
    setHistory(result);
  }, []);

  useEffect( () => {}, [history]);

  console.log(symbol);
  console.log(history);

  return history;
}
