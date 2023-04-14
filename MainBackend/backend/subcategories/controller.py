from flask import  jsonify, request, Blueprint
from backend.subcategories.model import SubCategory
from backend.db import db
from datetime import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


subcategories = Blueprint('subcategories', __name__, url_prefix='/subcategories')

#get all subcategories
@subcategories.route("/")
def all_subcategories():
    subcategories= SubCategory.query.all()
    return jsonify({
            "success":True,
            "data":subcategories,
            "total":len(subcategories)
        }),200



#creating subcategories
@subcategories.route('/create', methods= ['POST'])
@jwt_required()
def new_food_subcategory():

    data = request.get_json()
    name = data['name']
    category_id= data['category_id']
    created_by = get_jwt_identity()
      
  
    #validations
    if not name:
         return jsonify({'error':"Food subcategory name is required",'success':False}),400
    

    if SubCategory.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "Food subcategory name exists",'success':False}), 409 

    new_food_subcategory = SubCategory(name=name,category_id=category_id, created_by=created_by,created_at=datetime.now(),updated_at=datetime.now()) 
      
    #inserting values
    db.session.add(new_food_subcategory)
    db.session.commit()
    return jsonify({'message':'New food subcategory created successfully','data': new_food_subcategory}),201
          
   
  
    

#get,edit and delete food category by id
@subcategories.route('/food_subcategory/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_food_subcategory(id):
    food_subcategory = SubCategory.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":food_subcategory.id,
            "name": food_subcategory.name,
            "created_by":food_subcategory.created_by,
            "created_at": food_subcategory.created_at
          
        }
        return {"success": True, "subcategory": response,"message":"Food subcategory details retrieved"},200

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"Food subcategory name is required"}),400
    
        
        food_subcategory.name = data['name']
        food_subcategory.category_id = data['category_id']
        food_subcategory.updated_at = datetime.utcnow()
        db.session.add(food_subcategory)
        db.session.commit()
        return {"message": f"{food_subcategory.name}  Food subcategory updated successfully"},200

    elif request.method == 'DELETE':
        db.session.delete(food_subcategory)
        db.session.commit()
        return {"message": f"{food_subcategory.name} Food subcategory successfully deleted."},200  
  
        
  
   



