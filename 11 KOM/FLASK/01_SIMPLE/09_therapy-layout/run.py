from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/sign-up")
def signup():
    return render_template("sign-up.html")

@app.route("/<string:file>")
def filenotknown(file):
    return render_template("404.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "admin" and password == "12345678":
            return render_template("index.html")
    
        return render_template("login.html", err="Login Failed, Please try again!")

    return render_template("login.html")
    
if __name__ == '__main__':
    app.run(debug=True) #host="0.0.0.0", port=8000.