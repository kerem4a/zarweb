from flask import Flask 
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    zar=random.choice(['1','2','3','4','5','6','7','8','9','10'])
    return f'<h1>{zar}</h1>'

@app.route("/")
def fener():
    return '<h1>FENERBAHÇE</h1>'

app.run(debug=True)