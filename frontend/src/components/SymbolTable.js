import React, { useState, useEffect } from "react"
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

  useEffect(() => {
    fetch('http://https://blooming-journey-16393.herokuapp.com/ljwe/symbol/?freq=monthly&symbol_id=1')
    .then(res => res.json())
    .then(data => setOptions(data))
    .catch((err) => {console.error(err)})
    }, []);

    console.log('ping');

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
          {SymbolRow(options)}
        </tbody>
    </Table>
  )
}
