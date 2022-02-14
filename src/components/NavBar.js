import React from "react";
import { Container, Navbar, Nav, Button } from "react-bootstrap";
import Head from "next/head";
import Link from "next/link";

import gats from "../../public/gatsby.png";

export default () => {
  return (
    <Navbar fixed="top" bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="/">L.J.W.E</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Link className="nav-link" href="/about">
              About
            </Link>
            <Link className="nav-link" href="/dash">
              Dashboard
            </Link>
            <Link className="nav-link" href="/blog">
              Blog
            </Link>
          </Nav>
          <Nav>
            <Link href="/register">
              <Button variant="primary">Register</Button>
            </Link>
            <Link href="/login">
              <Button variant="outline-primary">Login</Button>
            </Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};
