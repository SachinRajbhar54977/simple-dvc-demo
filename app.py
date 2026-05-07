from flask import Flask, request, render_template, jsonify
import os
import joblib
from src.get_data import read_params

params_path = "params.yaml"
web_root = "webapp"

static_dir = os.path.join(web_root, "static")
template_dir = os.path.join(web_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]

    model = joblib.load(model_dir_path)
    prediction = model.predict(data)

    return prediction[0]


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            data = dict(request.form).values()
            data = [list(map(float, data))]

            print("Input Data:", data)

            prediction = round(float(predict(data)), 2)

            print("Final Prediction:", prediction)

        except Exception as e:
            print("Error:", e)
            error = "Something went wrong. Please check input values."

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )


@app.route("/predict", methods=["POST"])
def predict_api():
    try:
        data = request.get_json()

        features = [[
            float(data["fixed_acidity"]),
            float(data["volatile_acidity"]),
            float(data["citric_acid"]),
            float(data["residual_sugar"]),
            float(data["chlorides"]),
            float(data["free_sulfur_dioxide"]),
            float(data["total_sulfur_dioxide"]),
            float(data["density"]),
            float(data["pH"]),
            float(data["sulphates"]),
            float(data["alcohol"])
        ]]

        print("API Input Data:", features)

        prediction = round(float(predict(features)), 2)
        print(prediction)

        return jsonify({
            "success": True,
            "prediction": prediction
        })

    except Exception as e:
        print("API Error:", e)

        return jsonify({
            "success": False,
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
