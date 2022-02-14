import { Container, Row, Col, Button } from "react-bootstrap";
import { NavBar, Footer, PageLayout } from "../components";
import Head from "next/head";
import Link from "next/link";

export default function Home() {
  return (
    <Container align="center" style={{ border: "1px solid red" }}>
      <Row>
        <Col>
          <h1>Title</h1>
          <h3>This is a subtitle, for example, Welcome to LJWEquities.com!!</h3>
          <p>This is slightly larger</p>
          <Footer />
        </Col>
      </Row>
      <Row>
        <Col>
          <Link href="/about">
            <Button variant="outline-secondary" size="lg">
              Enter
            </Button>
          </Link>
        </Col>
      </Row>
    </Container>
  );
}
