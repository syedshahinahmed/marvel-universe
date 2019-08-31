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
    return render_template("index.html", superheros=mongo.db.superhero.find())

# About Route
@app.route('/about')
def about():
    return render_template("about.html", title='About', superheros=mongo.db.superhero.find())

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

# Edit Superhero Route
@app.route("/edit/<superhero_id>")
def edit(superhero_id):
    the_superhero = mongo.db.superhero.find_one(
        {'_id': ObjectId(superhero_id)})
    all_group = mongo.db.fav_superhero.find()
    return render_template('edit.html', title="Edit", superhero=the_superhero, group=all_group)


# Updating Individual Superhero
@app.route('/updateSuperhero/<superhero_id>', methods=["POST"])
def updateSuperhero(superhero_id):
    superheros = mongo.db.superhero
    superheros.update({'_id': ObjectId(superhero_id)}, {
        "group_name":request.form.get["group_name"],
        "name":request.form.get["name"],
        "description":request.form.get["description"],
        "species":request.form.get["species"],
        "gender":request.form.get["gender"],
        "affiliation":request.form.get["affiliation"],
        "status":request.form.get["status"],
        "poster":request.form.get["poster"],
        "superpowers":request.form.get["superpowers"]
    })
    return redirect(url_for(index))

 

# View Individual Superhero Route
@app.route('/viewsuperhero/<superhero_id>')
def viewsuperhero(superhero_id):
    the_superhero = mongo.db.superhero.find_one(
        {'_id': ObjectId(superhero_id)})
    all_group = mongo.db.fav_superhero.find()
    return render_template("viewsuperhero.html", title='View Superhero', superhero=the_superhero, group=all_group)


# test
# @app.route('/test')
# def test():
#     return render_template("test.html")


#####################
#### Deployment #####

if __name__ == "__main__":
    app.run(debug=True)
