from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User(db.Model):
  __tablename__ = 'users'

  id: int
  name: str
  email: str
  contact: str
  user_type: str

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255),nullable=False)
  email = db.Column(db.String(255))  
  contact = db.Column(db.String(255))
  user_type = db.Column(db.String(100))
  password = db.Column(db.String(255))
  created_at = db.Column(db.String(255), default=datetime.now())
  updated_at = db.Column(db.String(255),onupdate=datetime.now())
  addresses = db.Relationship("Address",backref="user")
  orders = db.Relationship("Order",backref="user")



  def __init__(self, name, email,contact,user_type,password, created_at,updated_at):
   self.name = name
   self.email = email
   self.contact = contact
   self.user_type = user_type
   self.password = password
   self.created_at = created_at
   self.updated_at = updated_at
  


  def __repr__(self):
        return f"<User {self.name} >"
  

