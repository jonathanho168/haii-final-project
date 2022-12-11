from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route('/predict/')
def predict():
    return '<h3>This is a Flask web application.</h3>'
