## Tutorial for how to render and create HTML templates

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/<name>")   #define como acessar esta página específica (poderia ser /home)
def home(name):
    return render_template("index.html", content=["Bugatti","Porsche","Mercedes Benz"],r=2)

if __name__ == '__main__':
    app.run(debug=True)