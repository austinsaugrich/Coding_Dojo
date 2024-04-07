// ParamComponent.js
import React from 'react';
import { useParams } from 'react-router-dom';
import NumberComponent from './NumberComponent';
import WordComponent from './WordComponent';

const ParamComponent = (props) => {
  const { input } = useParams();
    
  // Check if input is a number
  const isNumber = !isNaN(Number(input));
  console.log(isNumber)
  return (
    <div>
      {isNumber ? (
        <NumberComponent number={input} />
      ) : (
        <WordComponent word={input} />
      )}
    </div>
  );
};

export default ParamComponent;
