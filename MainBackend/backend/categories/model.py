from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Category(db.Model):
    __tablename__ = "categories"
    name:str
    image:str
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    image = db.Column(db.String(255),nullable=False)
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    sub_categories = db.Relationship("SubCategory", backref='category')
    created_at = db.Column(db.String(255),nullable=True, default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True, onupdate=datetime.now())
    
    def __init__(self,name,image,created_by,created_at,updated_at):
     self.image = image
     self.name = name
     self.created_by = created_by
     self.created_at = created_at
     self.updated_at = updated_at
    

    def __repr__(self):
        return f"<Category {self.name} >"
