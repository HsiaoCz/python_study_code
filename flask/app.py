from flask import Flask
from flask import render_template
from flask import Request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello,My man"


# 静态路由


@app.route("/index")
def index():
    return render_template("./index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = Request.form["name"]
    return "Hello" + name


if __name__ == "__main__":
    app.run(debug=True)
