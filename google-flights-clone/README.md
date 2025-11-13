# Flight Search Application

A simple flight search application built with React that allows users to find flights based on their travel preferences. This application utilizes the Sky Scraper API to fetch flight data.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Search for flights by origin, destination, and travel date.
- Display flight results with price, origin, destination, departure, and arrival times.
- Responsive design for optimal viewing on different devices.

## Demo

You can check out the live demo of the application here: [Live Demo Link](#)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flight-search-app.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd flight-search-app
   ```

3. Install the dependencies:
   ```bash
   npm install
   ```

4. Create a `.env` file in the root directory and add your RapidAPI key:
   ```plaintext
   REACT_APP_RAPIDAPI_KEY=your_rapidapi_key
   ```

5. Start the application:
   ```bash
   npm start
   ```

## Usage

1. Enter your travel details in the search form (origin, destination, date).
2. Click the "Search" button to fetch flight results.
3. View the available flights and their details.

## API

This application uses the [Sky Scraper API](https://rapidapi.com/sky-scrapper/api/sky-scrapper) to fetch flight data. Please ensure you have a valid API key to access the data.

### API Endpoint

- `GET https://sky-scrapper.p.rapidapi.com/api/v2/flights/searchFlightsWebComplete`

### Required Parameters

- `originSkyId`
- `destinationSkyId`
- `originEntityId`
- `destinationEntityId`
- `cabinClass`
- `adults`
- `sortBy`
- `currency`
- `market`
- `countryCode`
- `date`

## Technologies

- React
- Axios (for API requests)
- CSS
- dotenv (for environment variables)

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss changes or improvements.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


### Tips for Customization:
- **Features**: Add or remove features based on the functionality of your app.
