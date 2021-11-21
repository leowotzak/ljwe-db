import React, {useState} from "react"
import {Container, Row, Col} from "react-bootstrap"
import {LoginForm, NavBar} from "../components"
import Select from "react-select"



const options = [
  { value: 'chocolate', label: 'Chocolate' },
  { value: 'strawberry', label: 'Strawberry' },
  { value: 'vanilla', label: 'Vanilla' }
]



export default function Home() {

  const [searchOptions, setSearchOptions] = useState([])

  const handleChange = (e) => (
    console.log(e)
  )

  return (
  <Container align="center">


    <NavBar />



    <Row>
      <Col>
    <LoginForm />
    {/* <Select options={options} isMulti onChange={handleChange}/> */}
      </Col>
      </Row>
    </Container>
  )
}
