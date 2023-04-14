from flask import  jsonify, request, Blueprint
from backend.addresses.model import Address
from backend.db import db
from datetime import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

addresses = Blueprint('addresses', __name__, url_prefix='/addresses')

#get all addresses
@addresses.route("/")
def all_addresses():
    addresses= Address.query.all()
    return jsonify({
            "success":True,
            "data":addresses,
            "total":len(addresses)
        }),200



#creating addresses

@addresses.route('/create', methods= ['POST'])
@jwt_required()
def create_new_address():

    data = request.get_json()
    description = data['description']
    district_id = data['district_id']
    user_id =get_jwt_identity()
    
      
  
    #validations
    if not description:
         return jsonify({'error':"Address name is required"}),400
   
    if not district_id:
         return jsonify({'error':"District  name is required"}),400
    

    #check for an address with same district
    if  Address.query.filter_by(description=description).first() and Address.query.filter_by(user_id=user_id).first() and Address.query.filter_by(district_id=district_id).first():
        return jsonify({'error': "Address with this district name exists"}), 409 

    new_address =Address(description=description,user_id=user_id,district_id=district_id,created_at=datetime.now(),updated_at=datetime.now()) 
      
    #inserting values
    db.session.add( new_address)
    db.session.commit()
    return jsonify({'message':'New address created successfully','data': new_address}),201
          
   
  
    

#get,edit and delete address by id

@addresses.route('/address/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def handle_address(id):
    address = Address.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":address.id,
            "name": address.description,
            "user": address.user,
            "created_at": address.created_at
          
        }
        return {"success": True, "address": response,"message":"Address details retrieved"},200

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['description']:
            return jsonify({"message":"please enter your address"}),400
        
        if not data['district_id']:
            return jsonify({"message":"district name is required"}),400
        
        
        address.description = data['description']
        address.district_id = data['district_id']
        address.user_id = get_jwt_identity()
        address.updated_at = datetime.utcnow()
        db.session.add(address)
        db.session.commit()
        return {"message": f"{address.description} updated successfully"},200

    elif request.method == 'DELETE':
        db.session.delete(address)
        db.session.commit()
        return {"message": f"{address.description} successfully deleted."},200   
  
        
  
   



