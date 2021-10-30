from os import remove
from flask import Flask, request
from flask import json
from flask.json import jsonify
from flask_cors import CORS
import xmltodict
import xmltojson
from lxml.html.clean import Cleaner, clean_html

app = Flask(__name__)
CORS(app)


@app.route("/")
def helloWorld():
    return "Hello World!"


@app.post("/convert")
def convert():
    cleaner = Cleaner(
        scripts=True,
        javascript=True,
        page_structure=False,
        links=False,
        remove_tags=["img", "br"],
    )
    string = request.get_json()["string"]
    cleaned = cleaner.clean_html(string)
    cleaned = cleaned.replace('"', "'")
    result = xmltodict.parse(cleaned)
    # res = json.loads(result)
    return jsonify(result)
    # return cleaned


if __name__ == "__main__":
    app.run()
