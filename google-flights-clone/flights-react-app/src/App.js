import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Import your styles
import { fetchFlights } from './api/flights';
import SearchForm from './components/SearchForm';
import FlightResults from './components/FlightResults';

// Fetch airport details using the 'flights/auto-complete' endpoint
export const fetchAirportDetails = async (query) => {
  const options = {
    method: 'GET',
    url: 'https://sky-scanner3.p.rapidapi.com/flights/auto-complete',
    params: { query }, // e.g., "New York"
    headers: {
      'X-Rapidapi-Key': "8d64d710e6mshefe322287b21d89p1f5485jsn2cd68ce63117",
      'X-Rapidapi-Host': 'sky-scanner3.p.rapidapi.com',
    }
  };

  try {
    const response = await axios.request(options);
    // Use 'id' instead of 'skyId' for the airport identifier
    return response.data.data.map(airport => ({ id: airport.id }));
  } catch (error) {
    console.error('Error fetching airport details:', error);
    throw error;
  }
};

// Function to format the date in the required format (YYYY-MM-DD)
const formatDate = (date) => {
  const d = new Date(date);
  const year = d.getFullYear();
  const month = (`0${d.getMonth() + 1}`).slice(-2); // Add leading zero for month
  const day = (`0${d.getDate()}`).slice(-2); // Add leading zero for day
  return `${year}-${month}-${day}`; // Return formatted date
};

function App() {
  const [flights, setFlights] = useState([]);
  const [error, setError] = useState(null); // State to store error message

  // Handle search and make API request
  const handleSearch = async (from, to, date) => {
    try {
      // Fetch airport details
      const originDetails = await fetchAirportDetails(from);
      const destinationDetails = await fetchAirportDetails(to);

      // Fetch flights
      const flights = await fetchFlights(
        originDetails.id,
        destinationDetails.id,
        date
      );

      // Handle the flight data and update the state
      setFlights(flights);
      setError(null); // Clear any previous errors
    } catch (error) {
      console.error('Error fetching flights:', error);
      setError('Failed to fetch flights. Please try again later.');
    }
  };

  return (
    <div className="App">
      <h1>Flight Search</h1>
      {error && <div className="alert alert-danger">{error}</div>} {/* Display error if any */}
      <SearchForm onSearch={handleSearch} />
      <FlightResults flights={flights} />
    </div>
  );
}

export default App;