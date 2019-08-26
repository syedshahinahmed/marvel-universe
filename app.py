################
#### Imports ###
from flask import Flask, render_template, redirect, request, url_for



################
#### Config #####
app =  Flask(__name__)

################
#### Route #####
@app.route('/')
def index():
    return render_template("index.html")

#####################
#### Deployment #####

if __name__ == "__main__":
    app.run(debug=True)
