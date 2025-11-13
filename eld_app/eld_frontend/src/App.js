import React, { useState } from 'react';
import TripForm from './components/TripForm';
import TripMap from './components/TripMap';
import LogSheet from './components/LogSheet';
import './index.css';

function App() {
    const [tripData, setTripData] = useState(null);

    const handleSubmit = async (data) => {
        const response = await fetch('http://127.0.0.1:8000/api/calculate-trip/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });
        const result = await response.json();
        setTripData(result);
    };

    return (
        <div className="container">
            <h1>ELD Trip Planner</h1>
            <TripForm onSubmit={handleSubmit} />
            {tripData && (
                <>
                    <TripMap route={tripData.map_data} />
                    <div className="log-sheets">
                        {tripData.log_sheets.map((sheet, index) => (
                            <LogSheet key={index} logSheet={sheet} />
                        ))}
                    </div>
                </>
            )}
        </div>
    );
}

export default App;