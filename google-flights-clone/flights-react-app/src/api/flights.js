import axios from 'axios';

// Function to format the date in the required format (YYYY-MM-DD)
const formatDate = (date) => {
  const d = new Date(date);
  const year = d.getFullYear();
  const month = (`0${d.getMonth() + 1}`).slice(-2); // Add leading zero for month
  const day = (`0${d.getDate()}`).slice(-2); // Add leading zero for day
  return `${year}-${month}-${day}`; // Return formatted date
};

// Fetch flight details using the appropriate endpoint
export const fetchFlights = async (fromCode, toCode, date) => {
  const formattedDate = formatDate(date);
  const options = {
    method: 'GET',
    url: 'https://sky-scanner3.p.rapidapi.com/flights/search-one-way', // Default to one-way
    params: {
      fromEntityId: fromCode, // Use fromCode directly
      toEntityId: toCode, // Use toCode directly
      departDate: formattedDate,
    },
    headers: {
      'X-Rapidapi-Key': process.env.REACT_APP_RAPIDAPI_KEY,
      'X-Rapidapi-Host': 'sky-scanner3.p.rapidapi.com'
    }
  };

  // Check for 'everywhere' search (toCode === 'Atlanta (Any)')
  if (toCode === 'Atlanta (Any)') {
    options.url = 'https://sky-scanner3.p.rapidapi.com/flights/search-everywhere';
    delete options.params.toEntityId; // Remove toEntityId for 'everywhere'
  }

  try {
    const response = await axios.request(options);
    // Handle incomplete searches (if applicable)
    if (response.data.status === 'incomplete') {
      return handleIncompleteSearch(response.data.data.sessionId);
    }

    return response.data.data; // Return flight data
  } catch (error) {
    console.error('Error fetching flight data:', error);
    throw error;
  }
};

// Function to handle subsequent calls for incomplete searches (example)
async function handleIncompleteSearch(sessionId) {
  const response = await axios.get(`https://sky-scanner3.p.rapidapi.com/flights/search-incomplete`, {
    params: {
      sessionId,
    },
    headers: {
      'X-Rapidapi-Key': '8d64d710e6mshefe322287b21d89p1f5485jsn2cd68ce63117',
      'X-Rapidapi-Host': 'sky-scanner3.p.rapidapi.com',
    },
  });
  return response.data.data;
}