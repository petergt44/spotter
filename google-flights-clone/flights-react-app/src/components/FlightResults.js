import React from "react";
import { Container, Row, Col } from "react-bootstrap";

const FlightResults = ({ flights }) => {
    console.log('Flights prop:', flights); // Log the flights prop to check its value
    // Ensure flights is an array before using .map
    if (!Array.isArray(flights) || flights.length === 0) {
        return <div className="alert alert-info">No flights found</div>;
    }

    return (
        <Container>
            <Row>
                {flights.map((flight, index) => (
                    <Col md={6} key={index}>
                        <div className="card mb-3">
                            <div className="card-header">
                                <h5>Flight {index + 1}</h5>
                            </div>
                            <div className="card-body">
                                <p>Price: {flight.price.formatted}</p>
                                <p>Origin: {flight.legs[0].origin.name}</p>
                                <p>Destination: {flight.legs[0].destination.name}</p>
                                <p>Departure: {new Date(flight.legs[0].departure).toLocaleString()}</p>
                                <p>Arrival: {new Date(flight.legs[0].arrival).toLocaleString()}</p>
                            </div>
                        </div>
                    </Col>
                ))}
            </Row>
        </Container>
    );
};

export default FlightResults;