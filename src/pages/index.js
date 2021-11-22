import React, {useState} from "react"
import {Container, Row, Col, Pagination} from "react-bootstrap"
import {LoginForm, NavBar, FrequencySelector, SymbolTable} from "../components"
import {LineChart, Line} from 'recharts';
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

  const data = [{name: 'page A', uv: 400, pv: 2400, amt: 2400}, {name: 'page A', uv: 600, pv: 2400, amt: 2400}, {name: 'page A', uv: 1200, pv: 2400, amt: 2400}];

  return (
  <Container align="center">


    <NavBar />
    <FrequencySelector />


    <LineChart width={400} height={400} data={data}>
      <Line type="monotone" dataKey="uv" stroke="#8884d8" />
      </LineChart>


    <Select options={options} isMulti onChange={handleChange}/>

    <SymbolTable />
    </Container>
  )
}
