from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Region(db.Model):
    __tablename__ = "regions"
    
    name:str
    created_by:int
    created_at:str
    updated_at:str
  
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    districts = db.Relationship("District",backref="region")
    created_at = db.Column(db.String(255),nullable=True, default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True, default=datetime.now())
 
   

    def __init__(self,name,created_by,created_at,updated_at):
     self.name = name
     self.created_by = created_by
     self.created_at = created_at
     self.updated_at = updated_at
    

    def __repr__(self):
        return f"<Region {self.name} >"
