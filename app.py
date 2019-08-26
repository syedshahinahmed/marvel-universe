################
#### Imports ###
from flask import Flask, render_template, redirect, request, url_for


################
#### Config #####
app = Flask(__name__)

# Mongo Config 
app.config["MONGO_DBNAME"] = "marfever"
app.config["MONGO_URI"] = ""

################
#### Route #####
@app.route('/')
def index():

    return render_template("index.html")

# About Route
@app.route('/about')
def about():
    return render_template("about.html", title='About')

# Contact Route
@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')

# Add Superhero Route
@app.route('/addsuperhero')
def addsuperhero():
    return render_template("addchar.html", title='Add Superhero')

# Edit Superhero Route
@app.route('/editsuperhero')
def editsuperhero():
    return render_template("editchar.html", title='Edit Superhero')



#####################
#### Deployment #####


if __name__ == "__main__":
    app.run(debug=True)
