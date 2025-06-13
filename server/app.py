# server/app.py
from flask import Flask
from .config import init_app, db
from .models import restaurant, pizza, restaurant_pizza
from .controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller

def create_app():
    app = Flask(__name__)
    init_app(app)

    app.register_blueprint(restaurant_controller.bp)
    app.register_blueprint(pizza_controller.bp)
    app.register_blueprint(restaurant_pizza_controller.bp)

    return app
