
from flask import Flask, render_template, request
import model


app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def post_data():
    content = request.form
    if request.method == "POST":
        radius_mean = content["radius_mean"]
        radius_se = content["radius_se"]
        radius_worst = content["radius_worst"]

        texture_mean = content["texture_mean"]
        texture_se = content["texture_se"]
        texture_worst = content["texture_worst"]

        perimeter_mean = content["perimeter_mean"]
        perimeter_se = content["perimeter_se"]
        perimeter_worst = content["perimeter_worst"]

        area_mean = content["area_mean"]
        area_se = content["area_se"]
        area_worst = content["area_worst"]

        smoothness_mean = content["smoothness_mean"]
        smoothness_se = content["smoothness_se"]
        smoothness_worst = content["smoothness_worst"]

        compactness_mean = content["compactness_mean"]
        compactness_se = content["compactness_se"]
        compactness_worst = content["compactness_worst"]

        concavity_mean = content["concavity_mean"]
        concavity_se = content["concavity_se"]
        concavity_worst = content["concavity_worst"]

        points_mean = content["points_mean"]
        points_se = content["points_se"]
        points_worst = content["points_worst"]

        symmetry_mean = content["symmetry_mean"]
        symmetry_se = content["symmetry_se"]
        symmetry_worst = content["symmetry_worst"]

        fractal_dimension_mean = content["fractal_dimension_mean"]
        fractal_dimension_se = content["fractal_dimension_se"]
        fractal_dimension_worst = content["fractal_dimension_worst"]

        class_prediction = model.model_prediction(
            radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
            concavity_mean, points_mean, symmetry_mean,
            fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se,
            compactness_se, concavity_se, points_se, symmetry_se, fractal_dimension_se, radius_worst,
            texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst,
            points_worst, symmetry_worst, fractal_dimension_worst
        )

    return render_template("result.html", n=class_prediction)


@app.route("/breast_cancer_prediction", methods=['POST'])
def api_call():
    content = request.json
    if request.method == "POST":
        radius_mean = content["radius"]["mean"]
        radius_se = content["radius"]["se"]
        radius_worst = content["radius"]["worst"]

        texture_mean = content["texture"]["mean"]
        texture_se = content["texture"]["se"]
        texture_worst = content["texture"]["worst"]

        perimeter_mean = content["perimeter"]["mean"]
        perimeter_se = content["perimeter"]["se"]
        perimeter_worst = content["perimeter"]["worst"]

        area_mean = content["area"]["mean"]
        area_se = content["area"]["se"]
        area_worst = content["area"]["worst"]

        smoothness_mean = content["smoothness"]["mean"]
        smoothness_se = content["smoothness"]["se"]
        smoothness_worst = content["smoothness"]["worst"]

        compactness_mean = content["compactness"]["mean"]
        compactness_se = content["compactness"]["se"]
        compactness_worst = content["compactness"]["worst"]

        concavity_mean = content["concavity"]["mean"]
        concavity_se = content["concavity"]["se"]
        concavity_worst = content["concavity"]["worst"]

        points_mean = content["points"]["mean"]
        points_se = content["points"]["se"]
        points_worst = content["points"]["worst"]

        symmetry_mean = content["symmetry"]["mean"]
        symmetry_se = content["symmetry"]["se"]
        symmetry_worst = content["symmetry"]["worst"]

        fractal_dimension_mean = content["fractalDimensions"]["mean"]
        fractal_dimension_se = content["fractalDimensions"]["se"]
        fractal_dimension_worst = content["fractalDimensions"]["worst"]

        class_prediction = model.model_prediction(
            radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
            concavity_mean, points_mean, symmetry_mean,
            fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se,
            compactness_se, concavity_se, points_se, symmetry_se, fractal_dimension_se, radius_worst,
            texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst,
            points_worst, symmetry_worst, fractal_dimension_worst
        )

        return class_prediction
app.run(debug=True)

