from flask import Flask, render_template, request
from main import search 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/user/<userId>")
def profile(userId):
    return f"{userId}'s profile"

if __name__ == "__main__":
    app.run(debug=True)