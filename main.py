from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_page():
    with open("index.html", "r") as f:
        return f.read()

@app.route('/animals')
def animal_page():
    with open("animals.html", "r") as f:
        return f.read()

