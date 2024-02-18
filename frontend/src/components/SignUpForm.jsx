import React from "react";
import FormField from "./FormField";

const SignUpForm = ({ onSubmit, header, fields }) => {
  return (
    <div className="column">
      <form onSubmit={onSubmit}>
        <h1 className="Subtitle has-text-centered">{header}</h1>
        {fields?.map((field) => (
          <FormField
            key={field.name}
            type={field.type}
            name={field.name}
            value={field.value}
            onChangeClass={field.onChangeClass}
          ></FormField>
        ))}
        <button className="button is-primary" type="submit">
          Sign Up
        </button>
      </form>
    </div>
  );
};

export default SignUpForm;
