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
@app.route('/')
def index():
    return render_template("index.html",superheros=mongo.db.superhero.find())

# About Route
@app.route('/about')
def about():
    return render_template("about.html", title='About', superheros=mongo.db.superhero.find())

# Contact Route
@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')


# View Superhero Route
@app.route('/viewsuperhero/<url_for>')
def viewsuperhero(url_for):
    marvel = {}
    return render_template("viewsuperhero.html", title='View Superhero', superheros=mongo.db.superhero.find())

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
# @app.route('/editsuperhero/<superhero_id>')
# def editsuperhero(superhero_id):
#     new_superhero = mongo.db.superhero.find_one(
#         {"_id": ObjectId(superhero_id)})
#     all_group = mongo.db.fav_superhero.find()
#     return render_template("editsuperhero.html", title='Edit Superhero', superheros=new_superhero)


# Edit Superhero Route
@app.route("/editsuperhero")
def editsuperhero():
    return render_template('editsuperhero.html', title='Edit Superhero')

# Update Superhero


# test
# @app.route('/test')
# def test():
#     return render_template("test.html")


#####################
#### Deployment #####

if __name__ == "__main__":
    app.run(debug=True)
