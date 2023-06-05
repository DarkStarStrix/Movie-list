from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'

db = SQLAlchemy(app)
cursor = sqlite3.connect("movies.db")


# redirection
@app.route("/add", methods=["GET", "POST"])
def add():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("add.html")


@app.route("/find")
def find():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("find.html")


redirect(url_for("add"))
redirect(url_for("find"))

request.args.get("id")


# Create Table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


# Create Form
class FlaskForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if __name__ == '__main__':
        app.run(debug=True)
    form = FlaskForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(
            url=f"https://api.themoviedb.org/3/search/movie?api_key=8e1b6e2b8e5f1b3b2b6c6d7c1b4b5e2a&query={movie_title}")
        data = response.json()["results"]
        return render_template("select.html", data=data)
    return render_template("add.html", form=form)


@app.route("/find")
def find():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("find.html")


@app.route("/edit")
def edit():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("edit.html")


@app.route("/delete")
def delete():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("delete.html")


@app.route("/select")
def select():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("select.html")


@app.route("/select/<int:movie_id>")
def select_movie():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("select.html")


@app.route("/find/<int:movie_id>")
def find_movie():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("find.html")


@app.route("/edit/<int:movie_id>")
def edit_movie():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("edit.html")


@app.route("/delete/<int:movie_id>")
def delete_movie():
    if __name__ == '__main__':
        app.run(debug=True)
    return render_template("delete.html")


if __name__ == '__main__':
    app.run(debug=True)
