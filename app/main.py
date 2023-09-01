#main.py
from flask import Flask, request

# main.py
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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5005')


