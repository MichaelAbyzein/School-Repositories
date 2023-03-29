from flask import Flask, jsonify, redirect, url_for
import json

app = Flask(__name__)

@app.route("/")

def index():
    return "<h1>API Has Been Loaded!</h1>"

@app.route("/api/latest/weather")
def api_weather_latest():
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

