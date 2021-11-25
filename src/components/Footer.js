import {Container, Row, Col, Navbar} from 'react-bootstrap'


export default () => {
    return (
<Navbar bg="light" expand="lg" fixed="bottom">
  <Container>
          <Col sm={10} align="left">
      <p>Written with React & Next.js</p>
      </Col>
      <Col sm={2} align="right">
      <a href="https://github.com/">Github</a>&thinsp;
      <a href="https://www.leojwotzak.com/">Website</a>
      </Col>
  </Container>
</Navbar>
    )
}