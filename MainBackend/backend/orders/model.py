from backend.db import db
from dataclasses import dataclass

@dataclass
class Order(db.Model):
    __tablename__ = "orders"
    id:int
    quantity:int
    status:str
    address_id:int
    user_id:int
    food_item_id:int
    

    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Integer)
    status=db.Column(db.String(25), nullable=True)
    address_id = db.Column(db.Integer,db.ForeignKey('addresses.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_items.id'))
    


    def __init__(self, quantity,address_id,user_id,food_item_id,status):
     self.quantity = quantity
     self.address_id = address_id
     self.user_id = user_id
     self.food_item_id = food_item_id
     self.status=status
     
    

    def __repr__(self):
        return f"<Order {self.user_id} >"
