from flask import Flask, request, render_template
import os
import yaml
import joblib
import numpy as np
from src.get_data import read_params

params_path = "params.yaml"
web_root = "webapp"

static_dir = os.path.join(web_root, "static")
template_dir = os.path.join(web_root, "templates")


app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir "]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction)
    return prediction


def api_resonse(request):
    pass


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        # Get the form data
        try:
            if request.form:
                data = dict(request.form).values()
                data = [list(map(float, data))]
                response = predict(data)
                return render_template("index.html", prediction=response)
            elif request.json:
                response = api_resonse(request)

                return jsonify(response)

           
        except Exception as e:
           print(e)
           error = {"error": "something went wrong"}
    else:
        return render_template("index.html")
    
        
        # Load the model and make a prediction
        model = joblib.load("model.pkl")
        features = np.array([[feature1, feature2, feature3]])
        prediction = model.predict(features)[0]
        
        return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)