import { Container, Row, Col, Navbar } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGithub } from "@fortawesome/free-solid-svg-icons";

export default () => {
  return (
    <Navbar bg="light" expand="lg" fixed="bottom" style={{ height: "30px" }}>
      <Container>
        <div>Written with React & Next.js</div>
        <div>
          <FontAwesomeIcon icon={["fab", "fa-github"]}>sssss</FontAwesomeIcon>
          <a href="https://www.leojwotzak.com/">Website</a>
          <a href="https://github.com/leowotzak/ljwe-backend">Github</a>
        </div>
      </Container>
    </Navbar>
  );
};
