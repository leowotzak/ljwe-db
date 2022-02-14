import { Container } from "react-bootstrap";
import { NavBar, Footer } from "../components";

export default ({ children }) => {
  return (
    <Container
      align="center"
      style={{
        display: "flex",
        alignItems: "center",
        height: "100vh",
        border: "1px solid green",
      }}
    >
      <NavBar />
      {children}
      <Footer />
    </Container>
  );
};
