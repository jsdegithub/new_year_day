from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def new_year():
    return render_template('index.html')
