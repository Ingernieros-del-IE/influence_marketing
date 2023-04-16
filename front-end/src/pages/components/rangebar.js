import React, { useState } from 'react';
import './rangebar.css';

const RangeSlider = () => {
  const [value, setValue] = useState(10000);

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <div className="range-slider">
      <h3>Followers</h3>
      <input
        type="range"
        id="range"
        name="range"
        min="10000"
        max="10000000"
        step="10000"
        value={value}
        onChange={handleChange}
      />
      <div className="prange"><p>10000 to {value} followers</p></div>
    </div>
  );
};

export default RangeSlider;