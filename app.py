from flask import Flask
from flask import render_template, url_for, request, redirect, flash
from sqlalchemy import Column, Integer, Float, Date
from forms import AddBlackCard, AddWhiteCard
import os
import db


app = Flask(__name__)
app.config.update(DEBUG=True)
#app.config.update(DEBUG=True, WTF_CSRF_ENABLED=True)
app.config['SECRET_KEY'] = '66ea3dab727dfa20322ca91c32854073'

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
@app.route("/black_cards", methods=['POST', 'GET'])
def black_cards():
    form = AddBlackCard()
    if form.validate_on_submit():
        flash(f'Black card added!', 'success')
        return redirect(url_for('black_cards'))

    return render_template("black_cards.html", title="white cards", form=form)


#add white card
@app.route("/white_cards", methods=['POST', 'GET'])
def white_cards():
    form = AddWhiteCard()
    if form.validate_on_submit():
        flash(f'White card added!', 'success')
        return redirect(url_for('white_cards'))
    return render_template("white_cards.html", title="white cards", form=form)


if __name__ == '__main__':
    app.run(debug = True)