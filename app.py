from flask import Flask, url_for, request, render_template, session

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

