import {Container, Row, Col} from "react-bootstrap";
import {NavBar, Footer} from "../components"

export default Template = () => {

    return (
        <Container>
        <NavBar />
        <Link href="/dash">
          <a>this page!</a>
        </Link>
        <Footer />
  
        </Container>
    )
}