from flask import Blueprint

# Import all blueprints
from .restaurant_controller import restaurant_bp
from .pizza_controller import pizza_bp
from .restaurant_pizza_controller import restaurant_pizza_bp

# Create main API blueprint
api = Blueprint('api', __name__)

# Register all blueprints
api.register_blueprint(restaurant_bp)
api.register_blueprint(pizza_bp)
api.register_blueprint(restaurant_pizza_bp)