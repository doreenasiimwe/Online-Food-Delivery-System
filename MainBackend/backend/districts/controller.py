from flask import  jsonify, request, Blueprint
from backend.districts.model import District
from backend.db import db
from datetime import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

districts = Blueprint('districts', __name__, url_prefix='/districts')

#get all districts
@districts.route("/")
def all_districts():
    districts= District.query.all()
    return jsonify({
            "success":True,
            "data":districts,
            "total":len(districts)
        }),200



#creating districts

@districts.route('/create', methods= ['POST'])
@jwt_required()
def create_new_district():

    data = request.get_json()
    name = data['name']
    region_id = data['region_id']
    created_by =  get_jwt_identity()
      
  
    #validations and contraints
    if not name:
         return jsonify({'error':"District name is required",'success':False}),400
   
    if not region_id:
         return jsonify({'error':"District region name is required",'success':False}),400
    

    if District.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "District name exists"}), 409 
    
    


    new_district = District(name=name,created_by=created_by,region_id=region_id,created_at=datetime.now(),updated_at=datetime.now()) 
      
    #inserting values
    db.session.add( new_district)
    db.session.commit()
    return jsonify({'message':'New district created successfully','data': new_district}),201
          

#get,edit and delete district by id
@districts.route('/district/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_district(id):
    district = District.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":district.id,
            "name": district.name,
            "region": district.region,
            "created_by":district.created_by,
            "created_at": district.created_at
          
        }
        return {"success": True, "district": response,"message":"district details retrieved"},200

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"district name is required"}),400
        
        if not data['region_id']:
            return jsonify({"message":"district region name is required"}),400
        
        
        district.name = data['name']
        district.region_id = data['region_id']
        district.updated_at = datetime.utcnow()
        db.session.add(district)
        db.session.commit()
        return {"message": f"{district.name} updated successfully"},200

    elif request.method == 'DELETE':
        db.session.delete(district)
        db.session.commit()
        return {"message": f"{district.name} successfully deleted."},200 
  
        
  
   



