from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server import db

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['price', 'pizza_id', 'restaurant_id']
    if not all(field in data for field in required_fields):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    # Validate price range
    try:
        price = int(data['price'])
        if not (1 <= price <= 30):
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    except ValueError:
        return jsonify({"errors": ["Invalid price value"]}), 400
    
    # Check if restaurant and pizza exist
    restaurant = Restaurant.query.get(data['restaurant_id'])
    pizza = Pizza.query.get(data['pizza_id'])
    
    if not restaurant or not pizza:
        return jsonify({"errors": ["Restaurant or Pizza not found"]}), 404
    
    # Create new RestaurantPizza
    try:
        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        # Return the created relationship with nested pizza and restaurant data
        return jsonify({
            "id": restaurant_pizza.id,
            "price": restaurant_pizza.price,
            "pizza": pizza.to_dict(rules=('-restaurant_pizzas',)),
            "restaurant": restaurant.to_dict(rules=('-restaurant_pizzas',))
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400