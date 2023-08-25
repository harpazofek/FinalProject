import os
import logging
from pymongo import MongoClient
from flask import Flask, request, jsonify

app = Flask(__name__)

# Get MongoDB credentials from environment variables
MONGO_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

# Configure the MongoDB connection
client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@database-service:27017/")

# Access a specific database
db = client["request_db"]
collection = db["requests"]

def testdb():
    try:
        client.command('ismaster')
    except:
        return "Server not available"
    return "Hello from the MongoDB client!\n"

@app.route('/save_request', methods=['POST', 'GET'])

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
    
# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = app.logger

@app.route('/ping', methods=['GET'])
@app.route('/pong', methods=['POST'])

def pingpongfun():
    if request.method == 'GET':
        return '<h1> Ofek say\'s P1NG</h1>'
    if request.method == 'POST':
        return '<h1> Ofek say\'s P0NG</h1>'

def main():
    app.run(host="0.0.0.0", port=5200, debug=True)


if __name__ == '__main__':
    main()
