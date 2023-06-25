from flask import Flask, request

app = Flask(__name__)
@app.route('/ping', methods=['GET'])
@app.route('/pong', methods=['POST'])

def getstudents():
    if request.method == 'GET':
        return '<h1> Ofek say\'s P1NG</h1>'
    if request.method == 'POST':
        return '<h1> Ofek say\'s P0NG</h1>'

def main():
    app.run(host="0.0.0.0", port=5200, debug=True)


if __name__ == '__main__':
    main()
