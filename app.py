from flask import Flask, request
from flask import json
from flask.json import jsonify
from flask_cors import CORS
import xmltodict
import xmltojson

app = Flask(__name__)
CORS(app)


@app.route("/")
def helloWorld():
    return "Hello World!"


@app.post("/convert")
def convert():
    string = request.get_json()["string"]
    result = xmltodict.parse(string)
    # res = json.loads(result)
    return jsonify(result)


if __name__ == "__main__":
    app.run()
