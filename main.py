from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/animals')
def animal_page():
    animal_db = get_animal_db()
    return render_template('animals.html', animals=animal_db)


def get_animal_db():
    lines = None
    with open("./static/animals_page/animals_list.csv", "r") as f:
        lines = f.readlines()
    lines = [line.split(",") for line in lines]
    animal_db = []
    for idx,i in enumerate(lines):
        if idx > 0:
            current_animal = {
                "name": i[0],
                "link": i[1],
                }
            animal_db.append(current_animal)
    return animal_db
    
