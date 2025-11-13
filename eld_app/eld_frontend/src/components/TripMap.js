import React from 'react';
import { MapContainer, TileLayer, Polyline, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import polyline from 'polyline';

// Fix for default marker icon
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon-2x.png',
    iconUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png',
    shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png',
});

const TripMap = ({ route }) => {
    const positions = polyline.decode(route.route_path).map(coord => [coord[0], coord[1]]);

    return (
        <MapContainer center={positions[0]} zoom={5} style={{ height: '400px', width: '100%' }}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            />
            <Polyline positions={positions} color="blue" />
            {route.markers.map((marker, index) => (
                <Marker key={index} position={marker.location}>
                    <Popup>
                        {marker.type.charAt(0).toUpperCase() + marker.type.slice(1)}
                        {marker.duration && ` - ${marker.duration} hrs`}
                    </Popup>
                </Marker>
            ))}
        </MapContainer>
    );
};

export default TripMap;