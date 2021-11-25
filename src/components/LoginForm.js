import React from "react"
import { useState } from "react"
import { Form, Button } from "react-bootstrap"

export default () => {
  const [user, setUser] = useState({})

  const handleChange = e => {
    if (e.target.name === "email") {
      setUser({ ...user, email: e.target.value })
    } else if (e.target.name === "password") {
      setUser({ ...user, password: e.target.value })
    } else {
      console.error("unexpected name", e.target.name)
    }
  }

  const handleSubmit = e => {
    console.log(user)
    e.preventDefault()
  }

  return (
    <Form>
      <Form.Group style={{ margin: "5px" }}>
        <Form.Label>Email Address</Form.Label>
        <br />
        <Form.Control
          type="email"
          placeholder="Enter email"
          name="email"
          onBlur={handleChange}
        ></Form.Control>
        <Form.Text>test message</Form.Text>
      </Form.Group>

      <Form.Group style={{ margin: "5px" }}>
        <Form.Label>Password</Form.Label>
        <br />
        <Form.Control
          type="password"
          placeholder="Password"
          name="password"
          onBlur={handleChange}
        ></Form.Control>
        <br />
      </Form.Group>

      <Form.Group style={{ margin: "5px" }}>
        <Form.Check type="checkbox" label="Remember me" />
      </Form.Group>
      <Button variant="primary" type="submit" onClick={e => handleSubmit(e)}>
        Submit
      </Button>
    </Form>
  )
}
