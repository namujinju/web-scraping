from flask import Flask, render_template, send_file
from covid import extract_data, extract_date
from save import save_to_file

date = extract_date()
datas = extract_data()
save_to_file(datas, date)

app = Flask("COVID-19-global")
result_db = {}


@app.route("/")
def home():

    return render_template("home.html")


@app.route("/result")
def result():
    datas = extract_data()
    result_db[0] = datas

    return render_template("result.html", datas=datas)


@app.route("/export")
def export():
    date = extract_date()
    datas = result_db[0]
    save_to_file(datas, date)
    return send_file(f"COVID-19-{date}.csv")


app.run(host="0.0.0.0")
