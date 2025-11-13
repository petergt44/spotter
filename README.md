# Spotter

A collection of transportation and logistics applications including ELD (Electronic Logging Device) trip planning, fuel route optimization, and flight search capabilities.

## Overview

Spotter is a multi-project repository containing several full-stack applications focused on transportation and logistics:

1. **ELD App** - Electronic Logging Device trip planner for truck drivers
2. **Fuel Route API** - Fuel price and route optimization service
3. **Google Flights Clone** - Flight search and booking interface
4. **Task** - Additional utility applications

## Projects

### 1. ELD Trip Planner (`eld_app/`)

A full-stack application for truck drivers to plan trips while complying with Hours of Service (HOS) regulations.

**Features:**
- Trip planning with real-time route calculation
- Interactive map visualization with OpenStreetMap
- Automatic HOS compliance checks (70hrs/8days cycle)
- Fuel stop planning (every 1,000 miles)
- Auto-generated daily log sheets
- Pickup/drop-off time accounting
- Rest break enforcement

**Tech Stack:**
- Backend: Django 4.2, Django REST Framework
- Frontend: React 17.0.2, Leaflet
- Services: OSRM Routing, Nominatim Geocoding

**Documentation:** See [eld_app/README.md](eld_app/README.md) for detailed setup and usage.

### 2. Fuel Route API (`fuel_route_api/`)

A Django-based API service for fuel price tracking and route optimization.

**Features:**
- Fuel price data management
- Route optimization with fuel cost calculations
- CSV data import functionality
- RESTful API endpoints

**Tech Stack:**
- Django
- PostgreSQL/SQLite
- Management commands for data loading

### 3. Google Flights Clone (`google-flights-clone/`)

A React-based flight search application inspired by Google Flights.

**Features:**
- Flight search interface
- Real-time flight data
- Search form with date and location inputs
- Flight results display

**Tech Stack:**
- React
- Flight API integration

**Documentation:** See [google-flights-clone/README.md](google-flights-clone/README.md) for details.

### 4. Task (`task/`)

Additional utility applications and services.

## Quick Start

### ELD App

```bash
cd eld_app

# Backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend
cd eld_frontend
npm install
npm start
```

### Fuel Route API

```bash
cd fuel_route_api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py load_fuel_data
python manage.py runserver
```

### Google Flights Clone

```bash
cd google-flights-clone/flights-react-app
npm install
npm start
```

## Project Structure

```
spotter/
├── eld_app/                  # ELD Trip Planner
│   ├── api/                  # Django API app
│   ├── eld_app/             # Django project settings
│   ├── eld_frontend/        # React frontend
│   ├── manage.py
│   └── requirements.txt
├── fuel_route_api/           # Fuel Route API
│   ├── route/               # Django app
│   ├── fuel_route_api/      # Django project settings
│   ├── manage.py
│   └── files/               # Data files
├── google-flights-clone/     # Flight search app
│   └── flights-react-app/   # React application
├── task/                     # Utility applications
└── eldenv/                   # Virtual environment
```

## Common Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- PostgreSQL (for production)
- Redis (for Celery, if used)

### Environment Variables

Each project may require its own environment variables. Check individual project READMEs for specific requirements.

Example `.env` file:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

## API Documentation

- **ELD App**: Available at `http://localhost:8000/api/` when running
- **Fuel Route API**: Check individual project documentation

## Deployment

Each project can be deployed independently:

- **ELD App**: Backend on Heroku, Frontend on Vercel
- **Fuel Route API**: Django deployment (Heroku, AWS, etc.)
- **Google Flights Clone**: Static hosting (Vercel, Netlify)

See individual project READMEs for deployment instructions.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Contact

For questions or issues, please open an issue on GitHub.

