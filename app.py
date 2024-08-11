from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import os
app= Flask(__name__)
CORS(app)
#connection to build with the mongodb client
mongo_uri = os.getenv("MONGO_URI", "mongodb://mongodb:27017/CoRider")
client = MongoClient(mongo_uri)
db = client['CoRider']

@app.route('/test-connection', methods=['GET'])
def test_connection():
    try:
        client.admin.command('ping')
        return jsonify({"status": "MongoDB connection is successful!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#the home route for debug
@app.route('/')
def helloworld():
    return "<p>Assignment: Flask Application for CRUD operations on MongoDB</p><p>This api performs crud apis on user names</p>"

#the route for post and get users 
@app.route("/user",methods=['POST','GET'])
def postget():
    if request.method=="POST":
        body=request.json
        name=body['name']
        email=body['email']
        password=body['password']
        db['users'].insert_one({
            "name":name,
            "email":email,
            "password":password
        })
        return jsonify({
            "status":"successfully inserted"
        })
    if request.method=="GET":
        data=db['users'].find()
        dataJson=[]
        for item in data:
            name=item['name']
            id=item['_id']
            email=item['email']
            password=item['password']
            currData={
                "id":str(id),
                "name":name,
                "email":email,
                "password":password
            }
            
            dataJson.append(currData)
        return jsonify(dataJson)


@app.route("/user/<string:id>",methods=['PUT','DELETE','GET'])
def update(id):
    if request.method=="GET":
        result=db['users'].find_one({"_id":ObjectId(id)})
        name=result['name']
        email=result['email']
        password=result['password']
        id=result['_id']
        res=[]
        temp={
            "id":str(id),
            "name":name,
            "email":email,
            "password":password
        }
        res.append(temp)
        return jsonify(res)

    if request.method=="PUT":
        filter_id=db['users'].find_one({"_id":ObjectId(id)})
        body=request.json
        name=body['name']
        email=body['email']
        password=body['password']
        newbody={
            "$set":{
                "name":name,
                "email":email,
                "password":password
            }
        }
        result=db['users'].update_one(filter_id,newbody)
        return jsonify({"status":"updated"})

    if request.method=="DELETE":
        filter_id=db['users'].find_one({"_id":ObjectId(id)})
        result=db['users'].delete_one(filter_id)
        return jsonify({"status":"Deleted"})




if __name__=="__main__":
    app.run(debug=True,port=8080)