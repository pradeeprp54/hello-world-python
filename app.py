from flask import Flask

app = Flask(__name__)

@app.route("http://3.238.141.229")
def hello_world():
    return "<p>Hello, World!</p>"
