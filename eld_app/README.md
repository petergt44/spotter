# ELD Trip Planner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![React](https://img.shields.io/badge/React-17.0.2-blue)](https://reactjs.org/)

A full-stack application for truck drivers to plan trips while complying with Hours of Service (HOS) regulations. Generates electronic logging device (ELD) reports and displays optimized routes.

**[Live Demo](https://eld-frontend.vercel.app/)** | 

## Features

- 📍 Trip planning with real-time route calculation
- 🗺️ Interactive map visualization with OpenStreetMap
- ⏰ Automatic HOS compliance checks (70hrs/8days cycle)
- ⛽ Fuel stop planning (every 1,000 miles)
- 📄 Auto-generated daily log sheets
- 🚚 Pickup/drop-off time accounting (1 hour each)
- 🛑 Rest break enforcement (30min after 8hrs driving)

## Technologies

**Backend**  
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)
![Django REST](https://img.shields.io/badge/Django_REST-3.14-red)

**Frontend**  
![React](https://img.shields.io/badge/React-17.0.2-%2361DAFB?logo=react)
![Leaflet](https://img.shields.io/badge/Leaflet-1.7.1-green?logo=leaflet)

**Services**  
![OSRM](https://img.shields.io/badge/OSRM-Routing-orange)
![Nominatim](https://img.shields.io/badge/Nominatim-Geocoding-lightgrey)

## Installation

### Backend Setup

```bash
# Clone repository
git clone https://github.com/yourusername/eld-app.git
cd eld-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
echo "SECRET_KEY=your_secret_key_here" > .env
echo "DEBUG=True" >> .env

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

### Frontend Setup

```bash
cd eld_frontend

# Install dependencies
npm install

# Start development server
npm start
```

## API Documentation

**Endpoint:** `POST /api/calculate-trip/`

**Request Body:**
```json
{
  "current_location": "New York, NY",
  "pickup_location": "Philadelphia, PA",
  "dropoff_location": "Washington, DC",
  "current_cycle_used": 20
}
```

**Response:**
```json
{
  "route": {
    "distance": 225.5,
    "duration": 4.2,
    "stops": [
      {"type": "fuel", "location": [39.9526, -75.1652], "distance": 1000}
    ]
  },
  "log_sheets": [
    {
      "date": "2023-10-01",
      "grid": [
        {"start": 0, "end": 6, "status": "off_duty"},
        {"start": 6, "end": 7, "status": "on_duty_not_driving"}
      ]
    }
  ]
}
```

## Deployment

### Backend (Heroku)

```bash
# Create new Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set SECRET_KEY=your_production_secret_key
heroku config:set DEBUG=False

# Deploy
git push heroku main
```

### Frontend (Vercel)

1. Import GitHub repository into Vercel
2. Set environment variables in project settings:
   - `REACT_APP_API_URL=https://your-heroku-app.herokuapp.com`
3. Deploy!

## Compliance Features

| Regulation         | Implementation Detail                     |
|---------------------|-------------------------------------------|
| 14-Hour Window     | Automatic duty period tracking            |
| 11-Hour Driving    | Real-time driving time monitoring         |
| 30-Minute Break    | Enforced after 8 cumulative driving hours |
| 70hr/8day Cycle    | Rolling duty hours calculation            |
| Fuel Stops         | Auto-planned every 1,000 miles            |

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add some feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit a pull request

**Code Standards:**
- Backend: PEP8 compliance
- Frontend: ESLint rules enforced
- Commit messages: Conventional commits

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This application demonstrates HOS compliance concepts but should not be used for actual regulatory compliance. Always consult official FMCSA guidelines for professional use.

---

**Project Maintainers**  
[Gakungu](mailto:gakungu.peter@gmail.com)
