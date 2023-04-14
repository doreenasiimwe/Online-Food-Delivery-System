from backend.db import db
from dataclasses import dataclass

@dataclass
class District(db.Model):
    __tablename__ = "districts"
    name:str
    region_id:int
    created_by:int

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    region_id = db.Column(db.Integer,db.ForeignKey('regions.id'))
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    addresses = db.Relationship("Address",backref="district")
    created_at = db.Column(db.String(255),nullable=True)
    updated_at = db.Column(db.String(255),nullable=True)
   
   

    def __init__(self, name,region_id,created_by,created_at,updated_at):
     self.region_id = region_id
     self.name = name
     self.created_by = created_by
     self.created_at = created_at
     self.updated_at = updated_at
    

    def __repr__(self):
        return f"<District {self.name} >"
