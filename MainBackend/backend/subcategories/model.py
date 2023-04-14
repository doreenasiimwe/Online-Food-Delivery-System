from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SubCategory(db.Model):
    __tablename__ = "sub_categories"
    name:str
    category_id:int
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    category_id= db.Column(db.Integer,db.ForeignKey('categories.id'))
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    food_items = db.Relationship("FoodItem", backref='subcategory')
    created_at = db.Column(db.String(255),nullable=True,default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True,onupdate=datetime.now())
    
       

    def __init__(self,name,category_id,created_by,created_at,updated_at):
     
     self.name = name
     self.category_id= category_id
     self.created_by = created_by
     self.created_at = created_at
     self.updated_at = updated_at
     
    

    def __repr__(self):
        return f"<SubCategory {self.name} >"
