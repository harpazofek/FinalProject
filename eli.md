python3 -m venv venv
. venv/bin/activate


If you want to deactivate the environment, just run the following command:
deactivate


pip install Flask


requirements.txt
# requirements.txt
Flask==1.1.2

pip install -r requirements.txt




# main.py
from flask import Flask
app = Flask(__name__)

@app.route('/basic_api/hello_world')
def hello_world():
    return 'Hello, World!'



to run ----
export FLASK_APP=main.py
export FLASK_ENV=development
flask run    