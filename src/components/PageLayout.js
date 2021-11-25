import {Container, Row, Col} from "react-bootstrap";
import {NavBar, Footer} from "../components"

export default ({children}) => {

    return (
        <Container>
        <NavBar />
        {children}
        <Footer />
        </Container>
    )
}