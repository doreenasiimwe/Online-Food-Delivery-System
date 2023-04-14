#register a new user
from flask import  jsonify, request, Blueprint
from backend.users.model import User
from flask_jwt_extended import create_access_token
from backend.db import db
from datetime import datetime

from werkzeug.security import generate_password_hash,check_password_hash

users = Blueprint('users', __name__, url_prefix='/users')

#get all users
@users.route("/")
def all_users():
    users= User.query.all()
    return jsonify({
            "success":True,
            "data":users,
            "total":len(users)
        }),200

#user registration
@users.route('/register',methods=['POST'])
def create_user():
    data = request.get_json()
    
    if request.method == "POST":
          
      name = data['name']
      email = data['email']
      contact = data['contact']
      user_type = data['user_type']
      password = data['password']


  
      #validations
      if not contact:
              return jsonify({'error':"Contact is required"}),400
      
      if not name:
              return jsonify({'error':"Name is required"}),400
      

      if len(password) < 6:
            return jsonify({'error': "Password is too short"}), 400



      if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error': "Email is already in use"}), 409 

    
      if User.query.filter_by(contact=contact).first() is not None:
        return jsonify({'error': "Phone number is already in use"}),409
       

      #creating a hashed password in the database
      hashed_password = generate_password_hash(password,method="sha256")
      new_user = User(name=name,email=email,contact=contact,user_type=user_type,password=hashed_password,created_at=datetime.now(),updated_at=datetime.now()) 
      
      #inserting values
      db.session.add(new_user)
      db.session.commit()
      return jsonify({'message':'New user created successfully','data':new_user}),201
        



#user login
@users.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    user=User.query.filter_by(email=email).first()

    if not email or not password:
        return jsonify({"message":"Both email and password are required"}),400
    
    if user:
        password_hash= check_password_hash(user.password,password)
        if password_hash:
            access_token= create_access_token(identity=user.id)
            return jsonify({"message":"Successfully logged in a user","access_token":access_token,"user":user}),200
        else:
            return jsonify({"message":"Invalid password"}),400
    else:
        return jsonify({"message":"email address doesn't exist"}),400
    

@users.route('/user/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'GET':
        response = {
            "id":user.id,
            "name": user.name,
            "user_type":user.user_type,
            "email": user.email,
            "contact": user.contact,
            "created_at": user.created_at
            
        }
        return {"success": True, "user": response,"message":"User details retrieved"},200

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"Your name is required"}),400
        
        if not data['email']:
            return jsonify({"message":"Your email address is required"}),400
        
        if not data['contact']:
            return jsonify({"message":"Your contact is required"}),400
        
        if not data['password'] or len(data['password'])<6:
            return jsonify({"message":"Your password is required and must be greater than 6 characters"}),400
        
        user.name = data['name']
        user.email = data['email']
        user.contact = data['contact']
        user.password = generate_password_hash(data['password'])
        user.user_type = data['user_type']
        user.updated_at = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        return {"message": f"User details of {user.name} updated successfully"},200

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.name} successfully deleted."} ,200  
  


