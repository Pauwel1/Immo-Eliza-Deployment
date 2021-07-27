import os
from flask import Flask, request, jsonify
from model.schemas import get_parameters


app = Flask(__name__)


@app.route("/", methods = ["GET"])
def check():
    return "Alive!"

@app.route("/predict", methods = ["POST", "GET"])
def respond():
    df = get_parameters.response()
    print(f"Got {df}")
    return jsonify(df)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host = "0.0.0.0", threaded = True, port = port)