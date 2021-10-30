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
    cleaner2 = Cleaner(
        scripts=True,
        forms=False,
        javascript=True,
        page_structure=False,
        links=False,
        remove_tags=["img", "br"],
    )
    string = request.get_json()["string"]
    cleaned = cleaner.clean_html(string)
    cleaned2 = cleaner2.clean_html(string)
    cleaned = cleaned.replace('"', "'")

    added = []
    x = 0
    while x < len(cleaned2) - 6:
        if cleaned2[x : x + 6] == "<input":
            add = ""
            while cleaned2[x] != ">":
                # print(cleaned2[x])
                add += cleaned2[x]
                x += 1
            add += "></input>"

            added.append(xmltodict.parse(add))
        x += 1

    result = xmltodict.parse(cleaned)
    # print(added[1530:1536])
    # res = json.loads(result)
    return jsonify({"result": result, "inputs": added})


if __name__ == "__main__":
    app.run()
