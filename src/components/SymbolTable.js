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
<Table striped bordered hover>
  <thead>
    <tr>
      <th>#</th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Username</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <td>3</td>
      <td colSpan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</Table>





    // <Table>
    //   <thead>
    //     <tr>
    //       <th>#</th>
    //       <th>First Name</th>
    //       <th>Last Name</th>
    //       <th>Username</th>
    //     </tr>
    //     </thead>
    //     <tbody>
    //       {allSymbolData.map(i => SymbolRow(i))}
    //     </tbody>
    // </Table>
  )
}

