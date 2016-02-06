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

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/get_lyrics', methods=['POST'])
def get_lyrics():
    lyrics = request.form.get('lyrics')
    print('I think this worked')
    print(lyrics)
    return redirect('/main')

@app.route('/get_mood', methods=['POST'])
def get_mood():
    mood = request.form.get('mood')
    print(mood)
    return redirect('/main')

@app.route('/get_settings', methods=['POST'])
def get_settings():
    mood = request.form.get('mood')
    key = request.form.get('key')
    lyrics = request.form.get('lyrics')
    print(mood)
    print(key)
    print(lyrics)
    return redirect('/main')

@app.route('/get_key', methods=['POST'])
def get_key():
    key = request.form.get('key')
    print(key)
    return redirect('/main')

@app.route("/main")
@app.route("/")
def main():
    return render_template("main.html")

# @app.route("/getLyrics", method=['POST'])
# def getLyrics():
#     lyrics = request.form.get("lyrics")
#     return redirect('/')

if __name__ == "__main__":
    app.run()
