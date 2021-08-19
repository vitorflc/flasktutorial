## TUTORIAL 5  - SESSIONS AND STORING DATA TEMPORARILY - CREATING PERMANENT SESSIONS
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "aodfg9ewmn"
app.permanent_session_lifetime = timedelta(minutes=5)   #armazena por 5 dias os dados da sessão

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True   # define a sessão específica como permanente pelo tempo designado lá em cima
        user = request.form["nm"]
        session["user"] = user                  # assim como o request.form - armazena dados como dicionário no session[chave] = variável
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user= user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)  # remove do dicionário
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)