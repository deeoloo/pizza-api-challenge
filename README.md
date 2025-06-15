```markdown
# Pizza API 

## Setup

### 1. Install dependencies
```bash
pipenv install
pipenv shell
```

### 2. Database Setup
```bash
# Create PostgreSQL database
createdb pizza_restaurant

# Initialize migrations
export FLASK_APP=server:create_app
flask db init
flask db migrate -m "Initial tables"
flask db upgrade
```

### 3. Seed Sample Data
```bash
python -m server.seed
```

### 4. Run the Server
```bash
flask run
```

## API Endpoints

### Restaurants
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/restaurants` | Get all restaurants |
| GET | `/api/restaurants/<int:id>` | Get single restaurant |
| DELETE | `/api/restaurants/<int:id>` | Delete restaurant |

### Pizzas
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/pizzas` | Get all pizzas |

### Restaurant Pizzas
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/restaurant_pizzas` | Create pizza association |

## Example Requests

### Get all restaurants
```bash
curl http://localhost:5000/api/restaurants
```
Response:
```json
[
  {
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Main St"
  }
]
```

### Create restaurant pizza
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 3
}' http://localhost:5000/api/restaurant_pizzas
```
Success Response (201):
```json
{
  "id": 4,
  "pizza": {
    "id": 1,
    "ingredients": "Tomato sauce, Mozzarella, Basil",
    "name": "Margherita"
  },
  "price": 15,
  "restaurant": {
    "address": "789 Pine Rd",
    "id": 3,
    "name": "Slice of Heaven"
  },
  "restaurant_id": 3
}
```

## Validation Rules

### RestaurantPizza
- `price`: Must be between 1-30 (inclusive)
- `pizza_id`: Must reference existing pizza
- `restaurant_id`: Must reference existing restaurant

Error Response (400):
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

## Postman Setup

1. Import the collection:
   - Click "Import" in Postman
   - Select `challenge-1-pizzas.postman_collection.json`

2. Environment variables:
   - Create new environment called "Pizza API"
   - Add variable `base_url` with value `http://localhost:5000`

3. Available requests:
   - GET All Restaurants
   - POST Create Restaurant Pizza
   - DELETE Restaurant

## Database Schema

### Restaurants
- `id` (Integer, PK)
- `name` (String, unique)
- `address` (String)

### Pizzas
- `id` (Integer, PK)
- `name` (String)
- `ingredients` (String)

### RestaurantPizzas
- `id` (Integer, PK)
- `price` (Integer)
- `pizza_id` (Integer, FK)
- `restaurant_id` (Integer, FK)
```