import React from "react"
import { Table } from "react-bootstrap"


const SymbolRow = ({symbol_id, ticker, name, description, sector, asset_type}) => {

  return (
    <tr key={symbol_id}>
      <td>{symbol_id}</td>
      <td>{ticker}</td>
      <td>{name}</td>
      <td>{description}</td>
      <td>{sector}</td>
      <td>{asset_type}</td>
    </tr>
  )
}


export default ({allSymbolData}) => {

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
          {allSymbolData.map(i => SymbolRow(i))}
        </tbody>
    </Table>
  )
}

