from flask import  jsonify, request, Blueprint
from backend.categories.model import Category
from backend.db import db
from datetime import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


categories = Blueprint('categories', __name__, url_prefix='/categories')

#get all categories
@categories.route("/")
def all_categories():
    categories= Category.query.all()
    return jsonify({
            "success":True,
            "data":categories,
            "total":len(categories)
        }),200



#creating categories

@categories.route('/create', methods= ['POST'])
@jwt_required()
def new_food_category():

    data = request.get_json()
    name = data['name']
    image = data['image']
    created_by =  get_jwt_identity()
      
  
    #validations
    if not name:
         return jsonify({'error':"Food category name is required",'success':False}),400
    

    if Category.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "Food category name exists",'success':False}), 409 

    new_food_category = Category(name=name,created_by=created_by,image=image,created_at=datetime.now(),updated_at=datetime.now()) 
      
    #inserting values
    db.session.add(new_food_category)
    db.session.commit()
    return jsonify({'message':'New food category created successfully','data': new_food_category.name}),201
          
   
  
    

#get,edit and delete food category by id
@categories.route('/food_category/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_food_category(id):
    food_category = Category.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":food_category.id,
            "name": food_category.name,
            "created_by":food_category.created_by,
            "created_at": food_category.created_at
          
        }
        return {"success": True, "category": response,"message":"Food category details retrieved"},200

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"Food category name is required"}),400
    
        
        food_category.name = data['name']
        food_category.image = data['image']
        food_category.updated_at = datetime.utcnow()
        db.session.add(food_category)
        db.session.commit()
        return {"message": f"{food_category.name}  Food category updated successfully"},200

    elif request.method == 'DELETE':
        db.session.delete(food_category)
        db.session.commit()
        return {"message": f"{food_category.name} Food category successfully deleted."},200   
  
        
  
   



