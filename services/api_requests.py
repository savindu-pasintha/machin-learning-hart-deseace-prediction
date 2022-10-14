from flask import Flask, request, jsonify, make_response;
#from flask_restful import Resource, Api;
#from marshmallow import fields;
#from marshmallow_sqlalchemy import ModelSchema;

app = Flask(__name__)

#create krnw end point
@app.route('/api/v1/model', methods=['POST'])
def post_request_function():
    data = request.get_json();
    return make_response(jsonify({"key_name": data}),200);

@app.route('/api/v1/model', methods=['GET'])
def get_request_function():
    data = request.get_json();
    return make_response(jsonify({"key_name": data}),200);

@app.route('/api/v1/model/<id>', methods=['PUT'])
def update_request_function(id):
    data = request.get_json();
    return make_response(jsonify({"key_name": data}),200);

@app.route('/api/v1/model/<id>', methods=['DELETE'])
def delete_request_function(id):
    data = request.get_json();
    return make_response(jsonify({"key_name": data}),204);

#app run krnn flask run    