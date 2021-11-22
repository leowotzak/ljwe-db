import React, {useState} from "react"
import {Container, Row, Col, Pagination} from "react-bootstrap"
import {LoginForm, NavBar, FrequencySelector, SymbolTable} from "../components"
import Select from "react-select"

import 'bootstrap/dist/css/bootstrap.min.css';

import "../styles/global.scss"



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



    <SymbolTable />
    </Container>
  )
}
