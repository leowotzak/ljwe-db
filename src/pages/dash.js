import React, { useState, useEffect } from "react";
import { Row, Col } from "react-bootstrap";
import { NavBar, SymbolTable, PageLayout } from "../components";
import { LineChart, Line } from "recharts";
import Select from "react-select";

import { getSymbols } from "../lib/symbols";

export async function getStaticProps() {
  const allSymbolData = await getSymbols();

  return {
    props: { allSymbolData },
  };
}

export default function Dash({ allSymbolData }) {
  // allSymbolData.map(({name, ticker}) => console.log(name, ticker))

  const ph_data = [
    { name: "page A", uv: 400, pv: 2400, amt: 2400 },
    { name: "page A", uv: 600, pv: 2400, amt: 2400 },
    { name: "page A", uv: 1200, pv: 2400, amt: 2400 },
  ];

  const [options, setOptions] = useState([]);
  const [selection, setSelection] = useState([]);

  const handleChange = (e) => {
    setSelection(e);
  };

  useEffect(() => {
    setOptions(
      Array.from(allSymbolData, ({ symbol_id, name, ticker }) => ({
        value: symbol_id,
        label: `(${ticker}) `.concat(name),
      }))
    );
  }, []);

  return (
    <PageLayout>
      <Row>
        <Col>
      <LineChart width={400} height={400} data={ph_data}>
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
      </LineChart>
      </Col>
      <Col>
      <LineChart width={400} height={400} data={ph_data}>
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
      </LineChart>
      </Col>
      </Row>
      <Select options={options} isMulti onChange={handleChange} />
      {/* {SymbolTable(allSymbolData)} */}
    </PageLayout>
  );
}
