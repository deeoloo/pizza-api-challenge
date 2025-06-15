from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp, url_prefix='/api')
    app.register_blueprint(pizza_bp, url_prefix='/api')
    app.register_blueprint(restaurant_pizza_bp, url_prefix='/api')

    return app
