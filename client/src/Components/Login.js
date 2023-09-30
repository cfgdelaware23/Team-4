import React, { useState } from "react";

import Form from "react-bootstrap/Form";

import Button from "react-bootstrap/Button";




export default function Login() {

  const [phone, setPhoneNumber] = useState("");

  const [password, setPassword] = useState("");


  function handleSubmit(event) {

    event.preventDefault();

  }

  return (

    <div className= "flex flex-row justify-center items-center w-screen h-screen bg-ketchup">
       
        <div className = "flex flex-col justify-center items-center w-1/2 h-1/2">
      <Form onSubmit={handleSubmit}>

        <Form.Group>

          <Form.Label>Phone Number:</Form.Label>

          <Form.Control

            autoFocus

            type="tel"

            value={phone}

            onChange={(e) => setPhoneNumber(e.target.value)}

          />

        </Form.Group>

        <Form.Group size="lg" controlId="password">

          <Form.Label>Password:   </Form.Label>

          <Form.Control

            type="password"

            value={password}

            onChange={(e) => setPassword(e.target.value)}

          />

        </Form.Group>

        <Button block size="lg" type="submit" >

          Login

        </Button>

      </Form>
      </div>

    </div>

  );

}