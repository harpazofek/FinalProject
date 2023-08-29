import os
import logging
from pymongo import MongoClient
from flask import Flask, request, jsonify
from logging.handlers import RotatingFileHandler
from logconfig import setup_logging

# Set up logging
setup_logging()

app = Flask(__name__)

# Get MongoDB credentials from environment variables
MONGO_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

# Configure the MongoDB connection
client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@database-service:27017/")
logging.info(client)

# Access a specific database
db = client["request_db"]
collection = db["requests"]

def testdb():
    try:
        client.command('ismaster')
        logging.debug(client)
    except:
        return "Server not available"
    return "Hello from the MongoDB client!\n"

def save_request():
    try:
        # Extract data from the request
        data = {
            "method": request.method,
            "url": request.url,
            "headers": dict(request.headers),
            "data": request.data.decode('utf-8')
        }

        # Insert data into MongoDB collection
        result = collection.insert_one(data)

        return jsonify({"message": "Request saved", "request_id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ping', methods=['GET'])
@app.route('/pong', methods=['POST'])
@app.route('/save_request', methods=['POST', 'GET'])

def pingpongfun():
    if request.method == 'GET':
        return '<h1> Ofek say\'s P1NG</h1>'
    if request.method == 'POST':
        return '<h1> Ofek say\'s P0NG</h1>'

# In-memory storage for countries
countries = [
        {"name": "United States", "capital": "Washington, D.C.", "population": 331002651},
        {"name": "Canada", "capital": "Ottawa", "population": 37742154},
        {"name": "United Kingdom", "capital": "London", "population": 67886011},
        {"name": "Australia", "capital": "Canberra", "population": 25499884},
        {"name": "India", "capital": "New Delhi", "population": 1380004385}
    ]

@app.route('/countries', methods=['GET'])
def get_countries():
    return jsonify(countries)

@app.route('/countries', methods=['POST'])
def add_country():
    data = request.get_json()
    countries.append(data)
    return jsonify({"message": "Country added successfully"})

@app.route('/countries/<int:index>', methods=['PUT'])
def update_country(index):
    if index >= 0 and index < len(countries):
        data = request.get_json()
        countries[index] = data
        return jsonify({"message": "Country updated successfully"})
    else:
        return jsonify({"message": "Invalid index"})

@app.route('/countries/<int:index>', methods=['DELETE'])
def delete_country(index):
    if index >= 0 and index < len(countries):
        del countries[index]
        return jsonify({"message": "Country deleted successfully"})
    else:
        return jsonify({"message": "Invalid index"})

def main():
    app.run(host="0.0.0.0", port=5200, debug=True)

if __name__ == '__main__':
    main()
