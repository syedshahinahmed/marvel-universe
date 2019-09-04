################
#### Imports ###
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

################
#### Config #####
app = Flask(__name__)

# Mongo Config
app.config["MONGO_URI"] = "mongodb+srv://syedroot:Azasr00t@syedcluster-eyeen.mongodb.net/marfever?retryWrites=true&w=majority"
mongo = PyMongo(app)

################
#### Route #####

# Home Route
@app.route('/')
def index():
    return render_template("index.html", superheros=mongo.db.superhero.find())


# About Route
@app.route('/about')
def about():
    # Phase One
    p1 = mongo.db.movies.find({"phase": "Phase One"})
    # Phase Two
    p2 = mongo.db.movies.find({"phase": "Phase Two"})
    # Phase Three
    p3 = mongo.db.movies.find({"phase": "Phase Three"})

    # Phase Four
    # p4 = mongo.db.movies.find({"phase": "Phase Four"})

    return render_template("about.html", title='About', phaseone=p1, phasetwo=p2, phasethree=p3)


# Contact Route
@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')


# Add Superhero Route
@app.route('/addsuperhero')
def addsuperhero():
    return render_template("addsuperhero.html", title='Add Superhero', superheros=mongo.db.superhero.find())


# Insert Superhero Route
@app.route("/insertsuoerhero", methods=['POST'])
def insertsuoerhero():
    # Connecting To Superhero Database
    superheros = mongo.db.superhero

    # Adding Form Data To Superhero Database
    superheros.insert_one(request.form.to_dict())

    return redirect(url_for('index'))


# Edit Superhero Route
@app.route("/edit/<superhero_id>")
def edit(superhero_id):
    the_superhero = mongo.db.superhero.find_one(
        {'_id': ObjectId(superhero_id)})
    all_group = mongo.db.fav_superhero.find()
    return render_template('edit.html', title="Edit", superhero=the_superhero, group=all_group)


# View Individual Superhero Route
@app.route('/viewsuperhero/<superhero_id>')
def viewsuperhero(superhero_id):
    # Finding Individual Superhero From Superhero Database
    the_superhero = mongo.db.superhero.find_one(
        {'_id': ObjectId(superhero_id)})
    return render_template("viewsuperhero.html", title='View Superhero', superhero=the_superhero)


# Updating Individual Superhero
@app.route("/updatesuperhero/<superhero_id>", methods=["POST"])
def updatesuperhero(superhero_id):
    # Connecting To Superhero Database
    superheros = mongo.db.superhero

    # Getting Data From Superhero Database And Updating
    superheros.update({'_id': ObjectId(superhero_id)}, {
        "group_name": request.form.get("group_name"),
        "name": request.form.get("name"),
        "description": request.form.get("description"),
        "species": request.form.get("species"),
        "gender": request.form.get("gender"),
        "affiliation": request.form.get("affiliation"),
        "status": request.form.get("status"),
        "poster": request.form.get("poster"),
        "powers_and_abilities": request.form.get("powers_and_abilities")
    })
    return redirect(url_for("index"))


# Delete a Superhero from Database
@app.route('/deletesuperhero/<superhero_id>')
def deletesuperhero(superhero_id):
    mongo.db.superhero.remove({'_id': ObjectId(superhero_id)})
    return redirect(url_for('index'))


# View Movies
@app.route("/movie/<movie_id>")
def movie(movie_id):
    # Finding Individual Movie From movies Database
    the_movie = mongo.db.movies.find_one(
        {'_id': ObjectId(movie_id)})

    # Finding All Movies From Movies Database
    view_movie = mongo.db.movies.find()
    return render_template('movies.html', movie=the_movie)


#####################
#### Deployment #####

if __name__ == "__main__":
    app.run(debug=True)
