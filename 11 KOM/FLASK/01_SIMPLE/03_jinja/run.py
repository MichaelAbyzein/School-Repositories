from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    text = "Wow, it's down and above high..."
    return render_template("index.html", text=text)

app.run()