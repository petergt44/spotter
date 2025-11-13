import React, { useState } from 'react';

const TripForm = ({ onSubmit }) => {
    const [currentLocation, setCurrentLocation] = useState('');
    const [pickupLocation, setPickupLocation] = useState('');
    const [dropoffLocation, setDropoffLocation] = useState('');
    const [currentCycleUsed, setCurrentCycleUsed] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({
            current_location: currentLocation,
            pickup_location: pickupLocation,
            dropoff_location: dropoffLocation,
            current_cycle_used: currentCycleUsed,
        });
    };

    return (
        <form onSubmit={handleSubmit} className="trip-form">
            <input
                type="text"
                value={currentLocation}
                onChange={(e) => setCurrentLocation(e.target.value)}
                placeholder="Current Location"
                required
            />
            <input
                type="text"
                value={pickupLocation}
                onChange={(e) => setPickupLocation(e.target.value)}
                placeholder="Pickup Location"
                required
            />
            <input
                type="text"
                value={dropoffLocation}
                onChange={(e) => setDropoffLocation(e.target.value)}
                placeholder="Dropoff Location"
                required
            />
            <input
                type="number"
                value={currentCycleUsed}
                onChange={(e) => setCurrentCycleUsed(e.target.value)}
                placeholder="Current Cycle Used (Hrs)"
                min="0"
                max="70"
                required
            />
            <button type="submit">Calculate Trip</button>
        </form>
    );
};

export default TripForm;