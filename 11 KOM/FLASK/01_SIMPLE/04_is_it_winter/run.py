from flask import Flask, render_template

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now =datetime.now()

    winter = now.month == 12 and now.day == 1
    return render_template("index.html", winter=winter)

app.run(debug=True)