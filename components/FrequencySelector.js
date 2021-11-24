import React from 'react'
import { Pagination } from 'react-bootstrap'




export default () => {

    const frequencies = ["D", "W", "M", "1-min", "5-min", "15-min", "30-min", "60-min"];

    return (
        <Pagination>
            {frequencies.map((item, index) => (
                <Pagination.Item key={index}>{item}</Pagination.Item>
                ))}
        </Pagination>
    )
}