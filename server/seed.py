from server.config import db
from server.app import create_app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.session.query(RestaurantPizza).delete()
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()

    pizza1 = Pizza(name="Margherita", ingredients="Tomato, Cheese, Basil")
    pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Cheese, Pepperoni")
    db.session.add_all([pizza1, pizza2])

    rest1 = Restaurant(name="Luigi's", address="123 Napoli Street")
    db.session.add(rest1)

    rp = RestaurantPizza(price=10, pizza=pizza1, restaurant=rest1)
    db.session.add(rp)

    db.session.commit()
