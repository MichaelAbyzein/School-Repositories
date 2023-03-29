from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "I'm at home!"

@app.route("/about")
def about():
    return "Was in Slough, France"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return "Hello, {}. You need to touch grass, now.".format(name)

if __name__ == "__main__":
    app.run()