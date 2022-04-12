import React, { useState, useEffect} from 'react';
import axios from "axios";


axios.defaults.baseURL = 'http://localhost:8000';
const instance = axios.create();

export let fetch = async (url) => {
  try {
    const response = await instance.get(url);
    return response.data;
  } catch (error) {
    console.error(error);
  }
}
