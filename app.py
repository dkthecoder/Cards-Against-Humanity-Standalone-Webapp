from flask import Flask, url_for, request, render_template, session
import os
import db


app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug = True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )


db.init_app(app)

#landing page
@app.route("/")
def index():
    return render_template("index.html")


#add black card
@app.route("/add_black_card")
def add_black_card():
    return "<p>black card add</p>"


#add white card
@app.route("/add_white_card")
def add_white_card():
    return "<p>white card add</p>"
