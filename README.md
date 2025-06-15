```
# Pizza Restaurant API 

A RESTful API for managing pizza restaurants, their menus, and pizza offerings, built with Flask and PostgreSQL.

## Features

- RESTful endpoints for restaurants, pizzas, and their relationships
- Proper database relationships using SQLAlchemy
- Serialization with SQLAlchemy-serializer
- Flask-Migrate for database migrations
- Proper MVC architecture

## Tech Stack

- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Flask-Migrate
- **Serialization**: SQLAlchemy-serializer

## Setup Instructions

### Prerequisites

- Python 3.11+
- PostgreSQL 12+
- pipenv (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pizza-restaurant-api.git
   cd pizza-restaurant-api
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

3. Install dependencies:
   ```bash
   pipenv install
   pipenv shell
   ```

4. Set up database:
   ```bash
   # Create your PostgreSQL database first
   createdb pizza_restaurant

   # Initialize migrations
   export FLASK_APP=server:create_app
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Seed sample data:
   ```bash
   python -m server.seed
   ```

## Running the Application

```bash
pipenv run flask run
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Restaurants
- `GET /api/restaurants` - List all restaurants
- `GET /api/restaurants/<id>` - Get restaurant details
- `DELETE /api/restaurants/<id>` - Delete a restaurant

### Pizzas
- `GET /api/pizzas` - List all pizzas

### Restaurant Pizzas
- `POST /api/restaurant_pizzas` - Create a pizza association

## Project Structure

```
.
├── server/
│   ├── __init__.py       # App factory
│   ├── app.py            # Main app entry
│   ├── config.py         # Configuration
│   ├── models/           # Database models
│   │   ├── pizza.py
│   │   ├── restaurant.py
│   │   └── restaurant_pizza.py
│   ├── controllers/      # Route handlers
│   │   ├── pizza_controller.py
│   │   ├── restaurant_controller.py
│   │   └── restaurant_pizza_controller.py
│   └── seed.py          # Database seeder
├── migrations/          # Database migrations
├── .env.example         # Environment template
├── Pipfile              # Dependencies
└── README.md            # This file
```

## Testing

Run the test suite with:
```bash
pipenv run pytest
```

## Deployment

For production deployment, consider:

1. Using Gunicorn:
   ```bash
   pipenv install gunicorn
   gunicorn "server:create_app()" -w 4 -b :5000
   ```

2. Setting up proper production environment variables:
   ```bash
   FLASK_ENV=production
   SECRET_KEY=your-production-secret
   DATABASE_URL=postgresql://produser:prodpass@prod-host/prod-db
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
