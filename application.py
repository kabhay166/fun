from flask import Flask , url_for , render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/home.html")
def home():
    return render_template("home.html")

@app.route("/ascent-of-man.html")
def ascentOfMan():
    return render_template("ascent-of-man.html")

@app.route("/cosmos.html")
def cosmos():
    return render_template("cosmos.html")