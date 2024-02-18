import React from "react";

const Input = ({ type, name, value, onChangeClass }) => {
  return (
    <input
      type={type}
      placeholder={"Enter " + name}
      value={value}
      onChange={(e) => onChangeClass(e.target.value)}
      className="input"
      required
    />
  );
};

export default Input;
