from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    visible = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Todo {self.id}-{self.title}-{self.visible}>'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/animals')
def animals():
    animal_db = get_animal_db()
    return render_template('animals.html', animals=animal_db)


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")


@app.route('/todo')
def todo():
    todo_list = Todo.query.all()
    todo_shown = []
    count = 0
    for i in todo_list:
        if i.visible:
            count += 1
            todo_shown.append([i, count])
    return render_template('todo.html', todo_list=todo_shown)


@app.route('/todo/add', methods=['POST'])
def todo_add():
    title = request.form.get("title")
    if title != "":
        new_todo = Todo(title=title, complete=False, visible=True)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for("todo"))


@app.route('/todo/check/<int:todo_id>')
def todo_check(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("todo"))


@app.route('/todo/hide/<int:todo_id>')
def todo_hide(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.visible = not todo.visible
    db.session.commit()
    return redirect(url_for("todo"))


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


if __name__ == "__main__":
    db.create_all()
    app.run(host='localhost', port=5000, debug=False)

    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
