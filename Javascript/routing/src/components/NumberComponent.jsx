// components/NumberComponent.js
import React from 'react';
import { useParams } from 'react-router-dom';


const NumberComponent = () => {
  const { input } = useParams();

  return (
    <div>
      <h1>The number is: {input}</h1>
    </div>
  );
};

export default NumberComponent;
