from flask import Flask, render_template
from prestiges import extract_prestiges

app = Flask("PrestigesScrapper")


@app.route("/")
def home():
    prestiges_list = extract_prestiges()
    return render_template("home.html", prestiges=prestiges_list)


app.run(host="0.0.0.0")
