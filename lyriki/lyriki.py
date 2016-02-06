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

@app.route('/get_settings', methods=['POST'])
def get_settings():
    mood = request.form.get('mood')
    key = request.form.get('key')
    lyrics = request.form.get('lyrics')
    print(mood)
    print(key)
    print(lyrics)
    return redirect('/main')

@app.route("/main")
@app.route("/")
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()
