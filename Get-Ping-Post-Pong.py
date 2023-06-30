#main.py
from flask import Flask, request

# main.py
app = Flask(FlaskApp)


@app.route('/ping', methods=['GET', 'POST'])

def ping():
    if request.method == "GET":
	request.environ.get('UserIP', request.remote_addr)   
        return {
            'message': 'Pong' ,
            'method': request.method ,
	    'message': UserIP ,
	    'body': request.json

        }
    if request.method == "POST":
	request.environ.get('UserIP', request.remote_addr)   
        return {
            'message': 'Pong',
	    'message': UserIP ,
            'method': request.method,
	    'body': request.json
        }


if FlaskApp == 'FlaskApp':
    app.run(host='0.0.0.0')
