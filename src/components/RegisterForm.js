import React from "react"
import { useState } from "react"
import { Form, Button, Container, Row, Col } from "react-bootstrap"

export default () => {

    return (
        <Container align="left" style={{maxWidth: "700px"}}>
        <Form>
            <Form.Group>
                <Form.Label>Email Address</Form.Label>
                <Form.Control type="email"/>
                <Form.Text>Your email will be kept private</Form.Text>
            </Form.Group>
            <Form.Group>
                <Form.Label>Username</Form.Label>
                <Form.Control />
                <Form.Text>How you will be represented on site</Form.Text>
            </Form.Group>
            <Form.Group>
                <Form.Label>Password</Form.Label>
                <Form.Control type="password"/>
            </Form.Group>
            <Form.Group>
                <Form.Label>Confirm Password</Form.Label>
                <Form.Control type="password"/>
            </Form.Group>
            <Form.Group style={{ margin: "5px" }}>
                <Form.Check label="Subscribe to future updates"/>
                </Form.Group>
                <Row className="justify-content-center">
      <Button variant="primary" type="submit" onClick={e => handleSubmit(e)} style={{maxWidth: "200px"}}>
        Submit
      </Button>
      </Row>
        </Form>
        </Container>
    )
}