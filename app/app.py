import os
from flask import Flask, request
import pickle

app = Flask(__name__)

# Get correct base directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Build model path
model_path = os.path.join(BASE_DIR, "models", "housing_model.pkl")

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json['input']
    result = model.predict([data])
    return {"prediction": result.tolist()}


if __name__ == "__main__":
    app.run(debug=True)