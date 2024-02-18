import React, { useState } from "react";
import SignUpForm from "./SignUpForm";
// import ErrorMessage from "./ErrorMessage";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmedPassword, setConfirmedPassword] = useState("");
  // const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (password === confirmedPassword && password.length > 5) {
      console.log("created");
      // } else {
      //   setErrorMessage("Ensure Passwords are matched..");
    }
  };

  const fields = [
    { type: "text", name: "email", value: email, onChangeClass: setEmail },
    {
      type: "password",
      name: "password",
      value: password,
      onChangeClass: setPassword,
    },
    {
      type: "password",
      name: "confirmed password",
      value: confirmedPassword,
      onChangeClass: setConfirmedPassword,
    },
  ];

  return (
    <>
      <div className="column">
        <h1 className="title has-text-centered">Story Point Planner</h1>
      </div>
      <div className="column">
        <SignUpForm onSubmit={handleSubmit} header="Sign Up" fields={fields} />
      </div>
    </>
  );
};

export default Register;
