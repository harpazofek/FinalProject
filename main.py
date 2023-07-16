#main.py
from flask import Flask, request

# main.py
app = Flask(__name__)


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of entities' ,
            'method': request.method ,
            'body': request.json ,
            'path': request.path ,
            'URL':  request.host_url 

        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
		    'body': request.json
        }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5005')


