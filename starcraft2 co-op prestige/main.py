from flask import Flask, render_template
from prestiges import extract_prestiges
from commanders import extract_commanders

app = Flask("PrestigesScrapper")


@app.route("/")
def home():

    commanders = extract_commanders()
    # commanders = ["Jim_Raynor"]

    com_prestiges = {}

    for commander in commanders:
        com_prestiges[commander] = extract_prestiges(commander)

    return render_template("home.html", com_prestiges=com_prestiges)


app.run(host="0.0.0.0")
