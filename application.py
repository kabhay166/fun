from flask import Flask
from flask import render_template,redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("abhay.html")

@app.route("/Abhishek")
def abhishek():
    return "<h1>Abhishek is a very good friend of author</h1><ul><li>He is lovely</li><li>He also loves phyics.</li><li>He is currently studying in IIT.</li></ul>"

              