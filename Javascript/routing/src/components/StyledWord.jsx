// components/StyledWordComponent.js
import React from 'react';
import { useParams } from 'react-router-dom';

const StyledWord = () => {
  const { word, color, background } = useParams();

  return (
    <div style={{ color: color, backgroundColor: background }}>
      <h1>The word is: {word}</h1>
    </div>
  );
};

export default StyledWord;
