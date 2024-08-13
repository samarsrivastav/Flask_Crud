from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from app.config import Config

# Create a Blueprint for user-related routes
users_bp = Blueprint('users', __name__)

# MongoDB connection
client = MongoClient(Config.MONGO_URI)
db = client['CoRider']

@users_bp.route('/')
def helloworld():
    return "<p>Assignment: Flask Application for CRUD operations on MongoDB</p><p>This api performs crud apis on user names</p>"

@users_bp.route('/test-connection', methods=['GET'])
def test_connection():
    try:
        client.admin.command('ping')
        return jsonify({"status": "MongoDB connection is successful!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users_bp.route('/user', methods=['POST', 'GET'])
def postget():
    if request.method == "POST":
        body = request.json
        name = body['name']
        email = body['email']
        password = body['password']
        db['users'].insert_one({
            "name": name,
            "email": email,
            "password": password
        })
        return jsonify({"status": "successfully inserted"})
    
    if request.method == "GET":
        data = db['users'].find()
        data_json = []
        for item in data:
            curr_data = {
                "id": str(item['_id']),
                "name": item['name'],
                "email": item['email'],
                "password": item['password']
            }
            data_json.append(curr_data)
        return jsonify(data_json)

@users_bp.route("/user/<string:id>", methods=['PUT', 'DELETE', 'GET'])
def update(id):
    if request.method == "GET":
        result = db['users'].find_one({"_id": ObjectId(id)})
        if result:
            return jsonify({
                "id": str(result['_id']),
                "name": result['name'],
                "email": result['email'],
                "password": result['password']
            })
        else:
            return jsonify({"error": "User not found"})

    if request.method == "PUT":
        body = request.json
        name = body['name']
        email = body['email']
        password = body['password']
        result = db['users'].update_one(
            {"_id": ObjectId(id)},
            {"$set": {"name": name, "email": email, "password": password}}
        )
        if result.modified_count:
            return jsonify({"status": "updated"})
        else:
            return jsonify({"error": "User not found"})

    if request.method == "DELETE":
        result = db['users'].delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"status": "Deleted"})
        else:
            return jsonify({"error": "User not found"})
