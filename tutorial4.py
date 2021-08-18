## Tutorial 4: HTTP Methods (GET/POST) & Retrieving Form Data
# get - insecure way to get info - you don't care if people see it (link etc)
# post - secure way (form data, not going to be saved)
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")   #define como acessar esta página específica (poderia ser /home)
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]      #vai me dar o dado que foi inputado dentro de "nm" em login.html request.form vem como dicionário, portanto deve ser único
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
    app.run(debug=True)