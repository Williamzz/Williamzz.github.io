from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import lyriki_music
import string

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

    key = key.lower()
    notes = {'c':72,'d':74,'e':76,'f':77,'g':79,'a':81,'b':83}
    key = notes[key]

    lyriki_music.make_song_file(mood,key,lyrics)
    lyriki_music.play_song()
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
