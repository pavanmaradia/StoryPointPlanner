import React from "react";
import Input from "./InputTag";

const FormField = ({ type, name, value, onChangeClass }) => {
  return (
    <div className="field">
      <label className="label">{name.toUpperCase()}</label>
      <div className="control">
        <Input
          type={type}
          name={name}
          value={value}
          onChangeClass={onChangeClass}
        />
      </div>
    </div>
  );
};

export default FormField;
