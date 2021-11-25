import React from "react"
import { useState } from "react"
import { Form, Button } from "react-bootstrap"

export default () => {

    return (
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
                <Form.Check label="Subscribe to future updates"/>
        </Form>
    )
}