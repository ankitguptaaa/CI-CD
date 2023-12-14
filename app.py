from flask import Flask
from werkzeug.urls import url_quote
from jinja2 import Markup, escape


app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello CI/Cd Only World!"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
