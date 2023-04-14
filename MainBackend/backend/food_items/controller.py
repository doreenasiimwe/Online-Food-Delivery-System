from flask import Blueprint,request,jsonify
from backend.db import db
from backend.food_items.model import FoodItem
from datetime import datetime
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


food_items = Blueprint('food_items',__name__,url_prefix='/food_items')



#get all food_items
@food_items.route("/")
def all_food_items():
    food_items = FoodItem.query.all()
    
    response = [{
                "id":item.id,
                "name": item.name,
                "created_by":item.created_by,
                "created_at": item.created_at,
            }for item in food_items]
        
    return jsonify({"success":True,"data":response,"total":len(food_items)}),200

#creating FoodItems
@food_items.route('/create', methods= ['POST'])
@jwt_required()
def new_food_item():

    data = request.get_json()
    name = data['name']
    price = data['price']
    price_unit = 'UGX'
    image=data['image']
    sub_category_id=data['sub_category_id']
    stock_measure = data['stock_measure']
    created_by=get_jwt_identity()
      
  
    #validations
    if not name:
         return jsonify({'error':"FoodItem name is required"}),400
    

    if FoodItem.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "FoodItem name exists"}), 409 

    new_food_item = FoodItem(name=name,price=price,price_unit=price_unit,image=image,sub_category_id=sub_category_id,stock_measure=stock_measure,created_by=created_by,created_at=datetime.now(),updated_at=datetime.now()) 
      
    #inserting values
    db.session.add(new_food_item)
    db.session.commit()
    return jsonify({'message':'New FoodItem created successfully','data': [new_food_item.name,new_food_item.price]}),201
          

#get,edit and delete food item by id
@food_items.route('/food_item/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_food_item(id):
    food_item = FoodItem.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":food_item.id,
            "name": food_item.name,
            "created_by":food_item.created_by,
            "created_at": food_item.created_at 
        }
        return {"success": True, "item": response,"message":"Food item details retrieved"},200

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"Food item name is required"}),400
    
        
        food_item.name = data['name']
        food_item.price = data['price']
        food_item.image=data['image']
        food_item.sub_category_id=data['sub_category_id']
        food_item.stock_measure = data['stock_measure']
        food_item.updated_at = datetime.utcnow()
        db.session.add(food_item)
        db.session.commit()
        return {"message": f"{food_item.name}  Food item updated successfully"},200

    elif request.method == 'DELETE':
        db.session.delete(food_item)
        db.session.commit()
        return {"message": f"{food_item.name} Food item successfully deleted."},200  
  
        
  
   



        
  


