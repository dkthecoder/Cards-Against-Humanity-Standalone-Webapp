from flask import Flask, render_template, url_for, redirect, flash
from forms import AddBlackCard, AddWhiteCard

import blackcards, whitecards

app = Flask(__name__)


app.config.update(DEBUG=True)
app.config['SECRET_KEY'] = '66ea3dab727dfa20322ca91c32854073'


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
        blackcards.add_card(form.card.data)
        flash(f'Black card added!', 'success')
        return redirect(url_for('black_cards'))
    
    cards = blackcards.read_all()

    print(black_cards)
    return render_template("black_cards.html", title="white cards", form=form, black_cards=cards)


#add white card
@app.route("/white_cards", methods=['POST', 'GET'])
def white_cards():
    form = AddWhiteCard()
    if form.validate_on_submit():
        whitecards.add_card(form.card.data)
        flash(f'White card added!', 'success')
        return redirect(url_for('white_cards'))

    cards = whitecards.read_all()
    print(cards)

    return render_template("white_cards.html", title="white cards", form=form, white_cards=cards)


if __name__ == '__main__':
    app.run()