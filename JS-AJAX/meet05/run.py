from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/")

def index():
    return "<h1>We Have Money (Unlike A Certain...)</h1>"

@app.route("/api/latest/currency/latest")
def api_currency_latest():
    try:
        with open("data.json") as file:
            data = json.load(file)
    except:
        return jsonify({
            "status" : False
        })
    else:
        response = jsonify(data)
        response.headers.add("Access-Control-Allow-Origin", '*')
        return response


app.run(debug=True)

