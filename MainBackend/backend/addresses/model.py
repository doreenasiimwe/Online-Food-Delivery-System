from backend.db import db
from dataclasses import dataclass

@dataclass
class Address(db.Model):
    __tablename__ = "addresses"
    id:int
    description:str
    district_id:int
    user_id:int

    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(255),nullable=False)
    district_id = db.Column(db.Integer,db.ForeignKey('districts.id'))
    user_id  = db.Column(db.Integer,db.ForeignKey('users.id'))
    orders = db.Relationship("Order",backref="address")
    created_at = db.Column(db.String(255),nullable=True)
    updated_at = db.Column(db.String(255),nullable=True)
   

    def __init__(self, description, district_id, user_id,created_at,updated_at):
     self.district_id = district_id
     self.description = description
     self.user_id = user_id
     self.created_at = created_at
     self.updated_at = updated_at


    def __repr__(self):
        return f"<Address {self.description} >"
