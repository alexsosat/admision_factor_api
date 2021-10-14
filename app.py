from flask import Flask, render_template, request
import model


app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def post_data():
    if request.method == "POST":
        gre = request.form["gre"]
        gpa = request.form["gpa"]
        income = request.form["income"]
        gender = request.form["gender"]
        ethnic = request.form["ethnic"]
        rank = request.form["prestige"]

        class_prediction = model.model_prediction(
            gre, gpa, income, gender, ethnic, rank)

    return render_template("result.html", n=class_prediction)


@app.route("/model_prediction", methods=['POST'])
def api_call():
    content = request.json
    if request.method == "POST":
        gre = content["gre"]
        gpa = content["gpa"]
        income = content["income"]
        gender = content["gender"]
        ethnic = content["ethnic"]
        rank = content["prestige"]

        class_prediction = model.model_prediction(
            gre, gpa, income, gender, ethnic, rank)

    if class_prediction == 0:
        return "0"
    else:
        return "1"


app.run(debug=True)
