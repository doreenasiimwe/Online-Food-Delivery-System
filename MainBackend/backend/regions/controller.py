from flask import  jsonify, request, Blueprint
from backend.regions.model import Region
from backend.db import db
from datetime import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

regions = Blueprint('regions', __name__, url_prefix='/regions')

#get all regions
@regions.route("/")
def all_regions():
    regions= Region.query.all()
    
    return jsonify({
            "success":True,
            "data":regions,
            "total":len(regions)
        }),200

#creating regions
@regions.route('/create', methods= ['POST'])
@jwt_required()
def create_new_region():

    data = request.get_json()
    name = data['name']
    created_by =  get_jwt_identity()
      
  
    #validations and constraints
    if not name:
         return jsonify({'error':"Region name is required",'success':False}),400
    

    if Region.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "Region name exists",'success':False}), 409 

    new_region = Region(name=name,created_by=created_by,created_at=datetime.now(),updated_at=datetime.now()) 
      
    #inserting values/storing the new region
    db.session.add( new_region)
    db.session.commit()
    return jsonify({'message':'New region created successfully','data': new_region.name}),201
          
   
  
    

#getting,editing and deleting region by id
@regions.route('/region/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handling_region(id):
    region = Region.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":region.id,
            "name": region.name,
            "created_by":region.created_by,
            "created_at": region.created_at
          
        }
        return {"success": True, "region": response,"message":"Region details retrieved"},200

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"Region name is required"}),400
    
        
        region.name = data['name']
        region.updated_at = datetime.utcnow()
        
        db.session.add(region)
        db.session.commit()
        return {"message": f"{region.name} updated successfully"},200

    elif request.method == 'DELETE':
        db.session.delete(region)
        db.session.commit()
        return {"message": f"{region.name} successfully deleted."},200
  
        
  




