from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/Vansh")
def Vansh():
    return "Hello Vansh4"

app.run(debug=True)