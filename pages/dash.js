import React from "react"
import {Container} from "react-bootstrap"
import {NavBar, SymbolTable} from "../components"
import {LineChart, Line} from 'recharts';
import Select from "react-select"

import {getSymbols} from '../lib/symbols'


    
export async function getStaticProps() {

    const allSymbolData = await getSymbols()

    return {
        props: { allSymbolData }
    }
  }

export default function Dash(allSymbolData) {
  console.log(allSymbolData)

    const ph_data = [{name: 'page A', uv: 400, pv: 2400, amt: 2400}, {name: 'page A', uv: 600, pv: 2400, amt: 2400}, {name: 'page A', uv: 1200, pv: 2400, amt: 2400}];
    const options = [
        { value: 'chocolate', label: 'Chocolate' },
        { value: 'strawberry', label: 'Strawberry' },
        { value: 'vanilla', label: 'Vanilla' }
      ]

    return <Container>
    <NavBar />
    <LineChart width={400} height={400} data={ph_data}>
      <Line type="monotone" dataKey="uv" stroke="#8884d8" />
      </LineChart>
    <Select options={options} isMulti />
      first dash
    {SymbolTable(allSymbolData)}
    </Container>
}