from flask import jsonify,request,Blueprint
from backend.orders.model import Order
from backend.db import db
from datetime import datetime
from flask_jwt_extended import jwt_required

# creating a blueprint for orders
orders = Blueprint('orders',__name__,url_prefix='/orders')

#get all orders
@orders.route("/")
def all_orders():
    orders= Order.query.all()
    return jsonify({
            "success":True,
            "data":orders,
            "total":len(orders)
        }),200


# endpoint to create an order
@orders.route('/create', methods=['POST'])
@jwt_required()
def create_new_order():
    quantity=request.json['quantity']
    address_id = request.json['address_id']
    user_id = request.json['user_id']
    status = request.json['status']
    food_item_id= request.json['food_item_id']


# validating the created order
    if not quantity:
        return jsonify({'error':"quantity of item required"}),400

    if not address_id:
        return jsonify({'error':"address required"}),400
    

# storing an order
    new_order= Order(quantity=quantity,address_id=address_id,user_id=user_id,status=status,food_item_id=food_item_id)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'success':'You have successfully placed your order'}),201

#get,edit and delete food order by id
@orders.route('/order/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_order(id):
    order = Order.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            "id":order.id,
            "quantity": order.quantity,
            "address_id":order.address_id,
            "status":order.status
          
        }
        return {"success": True, "order": response,"message":"Food order details retrieved"},200

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['quantity']:
            return jsonify({"message":"Food order quantity is required"}),400
    
        if not data['address_id']:
            return jsonify({"message":"Food order address_id is required"}),400
    
        
        order.quantity = data['quantity']
        order.status = data['status']
        order.address_id = data['address_id']
        order.updated_at = datetime.utcnow()
        db.session.add(order)
        db.session.commit()
        return {"message": "Food order updated successfully"},200

    elif request.method == 'DELETE':
        db.session.delete(order)
        db.session.commit()
        return {"message": "Food order successfully deleted."},200  
  
        
  
   





        


