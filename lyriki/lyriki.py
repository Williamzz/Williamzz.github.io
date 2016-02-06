from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
# configuration
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
def hello():
    return "Hello World!"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()