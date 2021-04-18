from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/animals')
def animal_page():
    return render_template('animals.html')
