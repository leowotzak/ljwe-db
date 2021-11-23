import React, { useState, useEffect } from "react"
import { Table } from "react-bootstrap"


const SymbolRow = ({symbol_id, ticker, name, description, sector, asset_type}) => {

  console.log(symbol_id, ticker, name, description, sector, asset_type)

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


export default (data) => {

  const [options, setOptions] = useState({})

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
          {
            data.map(({node}) => SymbolRow(node))
          }
        </tbody>
    </Table>
  )
}

