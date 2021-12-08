import React from "react";
import { Container, Navbar, Nav, NavDropdown, Button } from "react-bootstrap";
import Head from "next/head";
import Link from "next/link";

export default () => {
  return (
    <Navbar className="mb-4" bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="/">L.J.W.E</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/about">About</Nav.Link>
            <Nav.Link href="/dash">Dashboard</Nav.Link>
            <Nav.Link href="/blog">Blog</Nav.Link>
          </Nav>
          <Nav>
            <Nav.Link>
              <Link href="/register">
                <Button variant="primary">Register</Button>
              </Link>
            </Nav.Link>
            <Nav.Link>
              <Link href="/login">
                <Button variant="outline-primary">Login</Button>
              </Link>
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};
