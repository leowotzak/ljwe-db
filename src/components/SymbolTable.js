import React from "react"
import { useState } from "react"
import { Table } from "react-bootstrap"


const SymbolRow = ({symbol_id, ticker, name, description, sector, asset_type}) => {
  return (
    <tr>
      <td>{symbol_id}</td>
      <td>{ticker}</td>
      <td>{name}</td>
      <td>{description}</td>
      <td>{sector}</td>
      <td>{asset_type}</td>
    </tr>
  )
}


export default () => {

  const [options, setOptions] = useState({})

  fetch('http://127.0.0.1:8000/ljwe/symbol/?freq=daily&symbol_id=0')
  .then(res => res.json())
  .then(data => setOptions(data))
  .catch((err) => {console.error(err)})

  return (
    <Table>
      <thead>
        <tr>
          <th>#</th>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Username</th>
        </tr>
        </thead>
        <tbody>
          {Object.entries(options).map(([index, row]) => SymbolRow(row))}
        </tbody>
    </Table>
  )
}
