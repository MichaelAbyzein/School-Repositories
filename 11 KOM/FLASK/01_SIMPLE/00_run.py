from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/schumander")
def schumander():
    return "A Wild Schumander Appeared! What would you do ?"

@app.route("/html")
def more_html():
    return "<h1> Heyya bucko! You're not supposed to be here!</h1>"

app.run(debug=True) # host="0.0.0.0", port="8000",