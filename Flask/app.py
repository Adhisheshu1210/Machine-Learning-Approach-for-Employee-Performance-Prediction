from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "gwp.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def get_productivity_label(value):
    if value < 0.50:
        return "Low Productive"
    elif value < 0.75:
        return "Medium Productive"
    else:
        return "Highly Productive"


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/submit", methods=["POST"])
def submit():
    try:
        # --- Read form values ---
        quarter = request.form.get("quarter")
        day = int(request.form.get("day"))
        targeted_productivity = float(request.form.get("targeted_productivity"))
        over_time = float(request.form.get("over_time"))
        idle_time = float(request.form.get("idle_time"))
        no_of_style_change = int(request.form.get("no_of_style_change"))
        month = int(request.form.get("month"))

        department = request.form.get("department")
        team = request.form.get("team")

        smv = float(request.form.get("smv"))
        incentive = float(request.form.get("incentive"))
        idle_men = float(request.form.get("idle_men"))
        no_of_workers = int(request.form.get("no_of_workers"))

        # --- Encodings ---
        dept_map = {"Sewing": 0, "Finishing": 1, "Cutting": 2}
        team_map = {"Team A": 0, "Team B": 1, "Team C": 2, "Team D": 3, "Team E": 4}
        quarter_map = {"Q1": 0, "Q2": 1, "Q3": 2, "Q4": 3}

        department_encoded = dept_map.get(department, 0)
        team_encoded = team_map.get(team, 0)
        quarter_encoded = quarter_map.get(quarter, 0)

        # --- 13-feature input vector ---
        features = np.array([[
            quarter_encoded,
            day,
            targeted_productivity,
            over_time,
            idle_time,
            no_of_style_change,
            month,
            department_encoded,
            team_encoded,
            smv,
            incentive,
            idle_men,
            no_of_workers
        ]])

        # --- Prediction ---
        prediction = model.predict(features)[0]
        prediction_value = round(float(prediction), 2)

        productivity_label = get_productivity_label(prediction_value)

        # ---- chart dataset (can be customized later) ----
        chart_data = {
            "target": targeted_productivity,
            "predicted": prediction_value,
            "idle_time": idle_time,
            "overtime": over_time,
            "incentive": incentive,
            "workers": no_of_workers
        }

        return render_template(
            "submit.html",
            productivity_label=productivity_label,
            prediction_value=prediction_value,
            chart_data=chart_data
        )

    except Exception as e:
        return render_template("submit.html", prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
