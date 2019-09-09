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
    return render_template("index.html", superheros=mongo.db.marvel_universe.find())


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
    return render_template("addsuperhero.html", title='Add Superhero', superheros=mongo.db.marvel_universe.find())


# Insert Superhero Route
@app.route("/insertsuperhero", methods=['POST'])
def insertsuperhero():
    # Connecting To Superhero Database
    superheros = mongo.db.marvel_universe

    # Adding Form Data To Superhero Database
    superheros.insert_one(request.form.to_dict())

    return redirect(url_for('index'))


# Edit Superhero Route
@app.route("/edit/<superhero_id>")
def edit(superhero_id):
    the_superhero = mongo.db.marvel_universe.find_one(
        {'_id': ObjectId(superhero_id)})
    # all_group = mongo.db.fav_superhero.find()
    return render_template('editsuperhero.html', title="Edit", superhero=the_superhero)


# View Individual Superhero Route
@app.route('/viewsuperhero/<superhero_id>')
def viewsuperhero(superhero_id):
    # Finding Individual Superhero From Superhero Database
    the_superhero = mongo.db.marvel_universe.find_one(
        {'_id': ObjectId(superhero_id)})
    return render_template("viewsuperhero.html", title='View Superhero', superhero=the_superhero)


# Updating Individual Superhero
@app.route("/updatesuperhero/<superhero_id>", methods=["POST"])
def updatesuperhero(superhero_id):
    # Connecting To Superhero Database
    superheros = mongo.db.marvel_universe

    # Getting Data From Superhero Database And Updating
    superheros.update({'_id': ObjectId(superhero_id)}, {
        "group_name": request.form.get("group_name"),
        "real_name": request.form.get("real_name"),
        "name": request.form.get("name"),
        "aliases": request.form.get("aliases"),
        "short_description": request.form.get("short_description"),
        "short_description": request.form.get("short_description"),
        "species": request.form.get("species"),
        "gender": request.form.get("gender"),
        "affiliation": request.form.get("affiliation"),
        "status": request.form.get("status"),
        "poster": request.form.get("poster"),
        "powers": {
            "p1": request.form.get("p1"),
            "p2": request.form.get("p2"),
            "p3": request.form.get("p3"),
            "other_powers": request.form.get("other_powers")
        },
        "abilities": {
            "a1": request.form.get("a1"),
            "a2": request.form.get("a2"),
            "a3": request.form.get("a3"),
            "other_abilities": request.form.get("other_abilities")
        },
        "shop_link": request.form.get("shop_link"),
        "char_page": request.form.get("char_page"),
        "m1": {
            "collection_name": request.form.get("m1_collection_name"),
            "title": request.form.get("m1_title"),
            "phase": request.form.get("m1_phase"),
            "homepage": request.form.get("m1_homepage"),
            "imdb_id": request.form.get("m1_imdb_id"),
            "genres": request.form.get("m1_genres"),
            "overview": request.form.get("m1_overview"),
            "poster_path": request.form.get("m1_poster_path"),
            "backdrop_path": request.form.get("m1_backdrop_path"),
            "production_companies": request.form.get("m1_production_companies"),
            "logo_path": request.form.get("m1_logo_path"),
            "language": request.form.get("m1_language"),
            "release_date": request.form.get("m1_release_date"),
            "tagline": request.form.get("m1_tagline"),
            "trailer_link": request.form.get("m1_trailer_link"),
            "movie_shop_link": request.form.get("m1_movie_shop_link")
        },
        "m2": {
            "collection_name": request.form.get("m2_collection_name"),
            "title": request.form.get("m2_title"),
            "phase": request.form.get("m2_phase"),
            "homepage": request.form.get("m2_homepage"),
            "imdb_id": request.form.get("m2_imdb_id"),
            "genres": request.form.get("m2_genres"),
            "overview": request.form.get("m2_overview"),
            "poster_path": request.form.get("m2_poster_path"),
            "backdrop_path": request.form.get("m2_backdrop_path"),
            "production_companies": request.form.get("m2_production_companies"),
            "logo_path": request.form.get("m2_logo_path"),
            "language": request.form.get("m2_language"),
            "release_date": request.form.get("m2_release_date"),
            "tagline": request.form.get("m2_tagline"),
            "trailer_link": request.form.get("m2_trailer_link"),
            "movie_shop_link": request.form.get("m2_movie_shop_link")
        },
        "m3": {
            "collection_name": request.form.get("m3_collection_name"),
            "title": request.form.get("m3_title"),
            "phase": request.form.get("m3_phase"),
            "homepage": request.form.get("m3_homepage"),
            "imdb_id": request.form.get("m3_imdb_id"),
            "genres": request.form.get("m3_genres"),
            "overview": request.form.get("m3_overview"),
            "poster_path": request.form.get("m3_poster_path"),
            "backdrop_path": request.form.get("m3_backdrop_path"),
            "production_companies": request.form.get("m3_production_companies"),
            "logo_path": request.form.get("m3_logo_path"),
            "language": request.form.get("m3_language"),
            "release_date": request.form.get("m3_release_date"),
            "tagline": request.form.get("m3_tagline"),
            "trailer_link": request.form.get("m3_trailer_link"),
            "movie_shop_link": request.form.get("m3_movie_shop_link")
        }
    })
    return redirect(url_for("index"))


# Delete a Superhero from Database
@app.route('/deletesuperhero/<superhero_id>')
def deletesuperhero(superhero_id):
    mongo.db.marvel_universe.remove({'_id': ObjectId(superhero_id)})
    return redirect(url_for('index'))


# View Movies
@app.route("/movie/<movie_id>")
def movie(movie_id):
    # Finding Individual Movie From movies Database
    the_movie = mongo.db.movies.find_one(
        {'_id': ObjectId(movie_id)})
    return render_template('movies.html', movie=the_movie)


# @app.route("/popularmovie/<movie_id>")
# def popularmovie(movie_id):
#     # Finding Individual Movie From movies Database
#     the_movie = mongo.db.marvel_universe.find_one(
#         {'movies': ObjectId(movie_id)})

#     return render_template('themovie.html', movie=the_movie)


#####################
#### Deployment #####
if __name__ == "__main__":
    app.run(debug=True)
