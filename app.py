################
#### Imports ###
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

################
#### Config #####
app = Flask(__name__)

# Mongo Config 
app.config["MONGO_URI"] = "mongodb+srv://syedroot:Azasr00t@syedcluster-eyeen.mongodb.net/marfever?retryWrites=true&w=majority"
mongo = PyMongo(app)

################
#### Route #####
@app.route('/')
def index():

    return render_template("index.html", superheros=mongo.db.superhero.find())

# About Route
@app.route('/about')
def about():
    return render_template("about.html", title='About', superheros=mongo.db.superhero.find())

# Contact Route
@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')


# View Superhero Route
@app.route('/viewsuperhero')
def viewsuperhero():
    return render_template("viewchar.html", title='View Superhero', superheros=mongo.db.superhero.find())

# Add Superhero Route
@app.route('/addsuperhero')
def addsuperhero():
    return render_template("addchar.html", title='Add Superhero')

# Edit Superhero Route
@app.route('/editsuperhero')
def editsuperhero():
    return render_template("editchar.html", title='Edit Superhero')

# test 
@app.route('/test')
def test():
    return render_template("test.html")



#####################
#### Deployment #####


if __name__ == "__main__":
    app.run(debug=True)
