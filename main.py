#main.py
from flask import Flask, request

# main.py
from flask import Flask
app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def entities():
    return {
        'message': 'This endpoint should return a list of entities',
        'method': request.method
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0')


