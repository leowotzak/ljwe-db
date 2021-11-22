import React, {useState} from "react"
import {LoginForm, NavBar, FrequencySelector, SymbolTable} from "../components"
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
    <FrequencySelector />



    <Row>
      <Col>
    <LoginForm />
    {/* <Select options={options} isMulti onChange={handleChange}/> */}
      </Col>
      </Row>
    </Container>
  )
}
