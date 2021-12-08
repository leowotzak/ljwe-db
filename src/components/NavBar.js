import { Container, Navbar, Nav, NavDropdown, Button } from "react-bootstrap";

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
                <Button variant="primary">Register</Button>
          <Link href="/dash">Dashboard</Link>
          </Nav.Link>
        <Nav.Link>
                <Button variant="outline-primary">Login</Button>
)
}