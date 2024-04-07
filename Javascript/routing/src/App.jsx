import React from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import Home from './components/Home';
import StyledWord from './components/StyledWord';
import ParamComponent from './components/ParamComponent';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/home" element={<Home/>} /> 
        <Route path="/:word/:color/:background" element={<StyledWord/>} />
        <Route path="/:input" element={<ParamComponent />} />
      </Routes>
    </BrowserRouter>
  );
};


export default App;
