from flask import Flask
from flask import render_template, url_for, request, redirect, flash
import os
import db


app = Flask(__name__)
app.config.update(DEBUG=True)
#app.config.update(DEBUG=True, WTF_CSRF_ENABLED=True)
#app.config['SECRET_KEY'] = '44ea3dab727dfa24322ca91c30854073'

#db.init_app(app)

#landing page
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html", title="welcome")

#Rules
@app.route("/rules", methods=['POST', 'GET'])
def rules():
    return render_template("rules.html", title="rules")

#play
@app.route("/play", methods=['POST', 'GET'])
def play():
    return render_template("play.html", title="play")

#add black card
@app.route("/add_black_card")
def add_black_card():
    return "<p>black card add</p>"


#add white card
@app.route("/add_white_card")
def add_white_card():
    return "<p>white card add</p>"


if __name__ == '__main__':
    app.run(debug = True)