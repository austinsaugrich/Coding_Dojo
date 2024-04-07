// components/WordComponent.js
import React from 'react';
import { useParams } from 'react-router-dom';

const WordComponent = () => {
  const { input } = useParams();

  return (
    <div>
      <h1>The word is: {input}</h1>
    </div>
  );
};

export default WordComponent;
