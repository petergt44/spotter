import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

const SearchForm = ({ onSearch }) => {
  const [from, setFrom] = useState('');
  const [to, setTo] = useState('');
  const [date, setDate] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!from.trim() || !to.trim()) {
      alert('Please enter valid origin and destination.');
      return;
    }

    if (!date) {
      alert('Please select a valid travel date.');
      return;
    }

    onSearch(from, to, date);
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group className="mb-3">
        <Form.Label>From</Form.Label>
        <Form.Control
          type="text"
          placeholder="From (e.g., New York or JFK)"
          value={from}
          onChange={(e) => setFrom(e.target.value)}
        />
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>To</Form.Label>
        <Form.Control
          type="text"
          placeholder="To (e.g., Los Angeles or LAX)"
          value={to}
          onChange={(e) => setTo(e.target.value)}
        />
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>Date</Form.Label>
        <Form.Control
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />
      </Form.Group>
      <Button type="submit" disabled={!from || !to || !date}>Search Flights</Button>
    </Form>
  );
};

export default SearchForm;