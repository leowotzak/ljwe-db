import React, {useState} from "react"
import {graphql} from "gatsby"
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



export default ({data}) => {

  const [searchOptions, setSearchOptions] = useState([])

  const handleChange = (e) => (
    console.log(e)
  )

  const ph_data = [{name: 'page A', uv: 400, pv: 2400, amt: 2400}, {name: 'page A', uv: 600, pv: 2400, amt: 2400}, {name: 'page A', uv: 1200, pv: 2400, amt: 2400}];
  const symbols = data.allRestApiLjweSymbol.edges

  return (
  <Container align="center">


    <NavBar />
    <FrequencySelector />


    <LineChart width={400} height={400} data={ph_data}>
      <Line type="monotone" dataKey="uv" stroke="#8884d8" />
      </LineChart>


    <Select options={options} isMulti onChange={handleChange}/>

    {SymbolTable(symbols)}
    </Container>
  )
}


export const query = graphql`
query {
  allRestApiLjweSymbol {
    edges {
      node {
        symbol_id
        name
        sector
        ticker
        asset_type
      }
    }
  }
}
`

