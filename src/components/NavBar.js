import React from "react"
import { Container, Navbar, Nav, NavDropdown } from "react-bootstrap"
import Head from 'next/head'
import Link from 'next/link'



export default () => {

return (
<Navbar className="mb-4" bg="light" expand="lg">
  <Container>
    <Navbar.Brand href="/">React-Bootstrap</Navbar.Brand>
    <Navbar.Toggle aria-controls="basic-navbar-nav" />
    <Navbar.Collapse id="basic-navbar-nav">
      <Nav className="me-auto">
            <Nav.Link href="/blog">Blog</Nav.Link>
        <Nav.Link>
          <Link href="/about">About</Link>
          </Nav.Link>
          <Nav.Link>
          <Link href="/dash">Dashboard</Link>
          </Nav.Link>
        <Nav.Link>
          <Link href="/login">Login</Link>
        </Nav.Link>
        <Nav.Link>
          <Link href="/register">Sign up</Link>
        </Nav.Link>
      </Nav>
    </Navbar.Collapse>
  </Container>
</Navbar>
)
}