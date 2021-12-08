import React, { useState, useEffect } from "react";
import { Container, Row, Col } from "react-bootstrap";
import { SymbolTable, PageLayout, FrequencySelector } from "../components";
import { LineChart, Line, XAxis, YAxis, CartesianGrid } from "recharts";
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
      <Container>
        <Row>
          <Col>
          <Select options={options} isMulti onChange={handleChange} />
          </Col>
        </Row>
        <Row>
          <FrequencySelector />
          </Row>
      <Row>
        <Col>
      <LineChart width={800} height={400} data={ph_data}>
        <XAxis />
        <YAxis />
        <CartesianGrid strokeDasharray="3 3" />

        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
      </LineChart>
      </Col>
      <Col>
      <LineChart width={400} height={400} data={ph_data}>
        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
      </LineChart>
      </Col>
      </Row>
      {SymbolTable(selection)}

      {/* {SymbolTable(allSymbolData)} */}
      </Container>
    </PageLayout>
  );
}
