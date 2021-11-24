from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from forms import AddBlackCard, AddWhiteCard
import csv
import os

app = Flask(__name__)

app.config.update(DEBUG=True)
app.config['SECRET_KEY'] = '66ea3dab727dfa20322ca91c32854073'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class BlackCards(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    content = db.Column(db.Text(500), nullable=False)

    def __repr__(self):
        return f"BlackCard('{self.id}', '{self.content}')"

class WhiteCards(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    content = db.Column(db.Text(500), nullable=False)

    def __repr__(self):
        return f"WhiteCard('{self.id}', '{self.content}')"



# open file for reading BLACK cards
with open('data/CAH - Black Cards.csv') as csvDataFile:
    # read file as csv file 
    csvReader = csv.reader(csvDataFile)
    # for every row, print the row
    for row in csvReader:
        bc = BlackCards(content = 'row')
        db.session.add(bc)
        db.session.commit()


# open file for reading BLACK cards
with open('data/CAH - White Cards.csv') as csvDataFile:
    # read file as csv file 
    csvReader = csv.reader(csvDataFile)
    # for every row, print the row
    for row in csvReader:
        wc = WhiteCards(content = 'row')
        db.session.add(wc)
        db.session.commit()



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
    db.create_all()