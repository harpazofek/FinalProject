import os
import logging
from flask import Flask, request, jsonify
from logging.handlers import RotatingFileHandler
from logconfig import setup_logging

#main.py

# Set up logging for 
setup_logging()

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    if request.method == "GET":
        return f'<H2> Method GET, you have pinged successfuly   <br><br> Have a nice DAY and pong to you <H2> \
                URL: {request.host_url}ping \
                <br><br> Project BY : Daniel, Eli, Ofek, Lior'  


@app.route('/pong', methods=['POST'])
def pong():
    if request.method == "POST":
        return f'<H2> Method POST, you have pinged successfuly  <br><br> Have a nice DAY <H2> \
               URL: {request.host_url}pong \
                <br><br> Project BY : Daniel, Eli, Ofek, Lior'  

# Storage for basic information
basic_info = [
        {"name": "Eli Levi", "city": "Rosh Hain", "ID": 331546518},
        {"name": "Daniel Shahnovich", "city": "Karnei Shomron", "ID": 324578981},
        {"name": "Lior Taub", "city": "Ramat Gan", "ID": 615478536},
        {"name": "Ofek Harpaz", "city": "Tel Aviv", "ID": 308696938},
    ]

@app.route('/basic_info', methods=['GET'])
def get_basic_info():
    return jsonify(basic_info)

@app.route('/basic_info_add', methods=['POST'])
def add_basic_info():
    data = request.get_json()
    basic_info.append(data)
    return jsonify({"message": "Basic info added successfully"})

@app.route('/basic_info_/<int:index>', methods=['PUT'])
def update_basic_info(index):
    if index >= 0 and index < len(basic_info):
        data = request.get_json()
        basic_info[index] = data
        return jsonify({"message": "Basic info updated successfully"})
    else:
        return jsonify({"message": "Invalid index"})

@app.route('/basic_info/<int:index>', methods=['DELETE'])
def delete_basic_info(index):
    if index >= 0 and index < len(basic_info):
        del basic_info[index]
        return jsonify({"message": "Basic info deleted successfully"})
    else:
        return jsonify({"message": "Invalid index"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5005')