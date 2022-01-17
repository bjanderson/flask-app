from app import app
from flask import redirect, render_template, url_for


@app.route("/")
@app.route('/index')
def home():
    return render_template("index.html")

@app.route("/404")
@app.errorhandler(404)
def not_found(error=None):
    return render_template("404.html")

@app.route("/favicon.ico")
def favicon():
    return redirect(url_for("static", filename="favicon.ico"))
