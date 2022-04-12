/* TODO:
 *
 * Make the react-select list searchable by label AND symbol
 *
 * (maybe not needed) load default value from just symbol
 *
 * Make react-select display symbol (value) as the label
 *
 */

import React, { Component, useState, useEffect} from 'react';
import axios from 'axios';
import Graph from './Graph';
import { fetch } from './hooks/fetch';
import { useSymbol } from './hooks/useSymbol';
import Select from 'react-select'
//import AsyncSelect from 'react-select/async';

function Main() {

  const [symbol, setSymbol] = useState("MSFT");
  const symbolChange = (value) => {
    const symbol = value.value;
    console.log("handled change: ", value.value);
    setSymbol(symbol);
  }

  const [symbols, setSymbols] = useState([]);
  useEffect(async () => {
    const result = await fetch('/symbols');
    setSymbols(result);
  }, []);
//  useEffect( () => {}, [symbols]); // is this needed?

  const [info, setInfo] = useState([]);
  useEffect(async () => {
    const result = await fetch('/info/' + symbol);
    setInfo(result);
  }, [symbol]);
  //useEffect( () => {}, [info]);
  console.log(info);

  const [history, setHistory] = useState([]);
  useEffect(async () => {
    const result = await fetch('/history/' + symbol);
    console.log(symbol);
    setHistory(result);
  }, [symbol]);
  //useEffect( () => {}, [history]); //what does this do? why is it needed?



  return (
    <main>
      <div id="controls">
        <Select
          defaultValue = {{ value: "MSFT", label: "Microsoft Corporation" }}
          options={symbols}
          onChange={symbolChange}
        />
      </div>
	  <div id="inner">
      <div id="info">
        <p>Symbol: {info.symbol}</p>
        <p>Name: {info.name}</p>
      </div>
      <div id="graph">
        <Graph data={history} />
      </div>
      </div>
    </main>
  );
}

export default Main;

