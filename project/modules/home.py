# modules/home.py
from bottle import Bottle, route, template

app = Bottle()

@app.route('/')
def home():
    return template('views/home.html')
