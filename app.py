
from flask import Flask
from flask_cors import CORS
from flask import Flask, render_template

app = Flask(__name__,static_folder="static",template_folder="templates")
CORS(app)

@app.route("/checkAgent.html")
def equipo_html():
    return render_template("checkAgent.html")

@app.route("/")
def home():
    return render_template("checkAgent.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)