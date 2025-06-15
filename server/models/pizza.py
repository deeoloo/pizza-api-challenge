from server import db
from sqlalchemy_serializer import SerializerMixin

class Pizza(db.Model, SerializerMixin):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship("RestaurantPizza", back_populates="pizza", cascade="all, delete")

    serialize_rules = ('-restaurant_pizzas.pizza',)

    def __repr__(self):
        return f"<Pizza {self.id}: {self.name}>"
