import pygame
from midiutil.MidiFile import MIDIFile
import random

TRACK = 0
CHANNEL = 0
DURATION = 1
LOW = 50
HIGH = 100

notes = {'c':72,'d':74,'e':76,'f':77,'g':79,'a':81,'b':83}
midi = {60:'c',62:'d',64:'e',65:'f',67:'g',69:'a',71:'b'}
c = [60,64,67]
f = [60,65,69]
g = [55,62,65]
happy1 = [c,c,c,c,f,f,f,f,g,g,g,g,c,c,c,c,f,f,f,f,g,g,g,g,g,g,g,g,c,c,c,c]

########################### Next Note ###############################

# helper function
# add these to MIDI notes
def chordType(chord):
    if chord == "m":
        return [ -12, -9, -5, 0, 3, 7, 12]
    elif chord == "M7":
        return [ -12, -8, -5, -1, 0, 4, 7, 11, 12]
    elif chord == "M":
        return [ -12, -8, -5, 0, 4, 7, 12]

# helper function
# enters int
def compatibleNotesToChord(key, chord):
    scales = chordType(chord)
    for i in range(len(scales)):
        scales[i] += key
    return scales

# helper function
def nearestTo(number, listOfNum):
    count = 1000
    closest = None
    for i in listOfNum:
        if abs(number-i) < count:
            count = abs(number-i)
            closest = i
    return closest

def generateNextNote(prevNote, chord, key):
    noteList = compatibleNotesToChord(key, chord)
    prevNote += random.triangular(-9, 9, 0)
    newNote = nearestTo(prevNote, noteList)
    return newNote

def generateNeighbor(dist,num):
    rand = random.random()
    if (dist == 0):
        if (num == 1):
            return [0]
        if (num == 2):
            if (rand < 0.5):
                return [0,1]
            else:
                return [0,-1]
        if (num == 3):
            if (rand < 0.5):
                return [0,-1,1]
            else:
                return [0,1,-1]
    else:
        return None

######################## Create and Play MIDI File ######################

def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print "Music file %s loaded!" % music_file
    except pygame.error:
        print "File %s not found! (%s)" % (music_file, pygame.get_error())
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

def play_song():
    # pick a midi music file you have ...
    # (if not in working folder use full path)
    music_file = "song.mid"
    '''
    freq = 44100    # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 1024    # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)
    '''
    pygame.mixer.init()
    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)
    try:
        play_music(music_file)
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit

#precondition: mood specifies a chord progression
#precondition: key specifies a key
#precondition: syllables is a list of ints representing syllables of words
def make_song_file(mood,key,syllables):
    # create the MIDIFile object with 1 track
    MyMIDI = MIDIFile(1)
    syllables = [2,1,2,3,2,1,2,3,1,1,2,2,1,1,1,3,2,1,2,3,2,2,2,2,1,1,1,3,2,1,1,2]
    mood = happy1

    # tracks are numbered from zero. times are measured in beats.

    track = 0   
    time = 0

    # add track name and tempo.
    MyMIDI.addTrackName(track,time,"Sample Track")
    MyMIDI.addTempo(track,time,100)

    key = key%12
    MyMIDI = add_chords(MyMIDI,mood,key)
    MyMIDI = add_notes(MyMIDI,syllables,key,mood)

    # and write it to disk.
    binfile = open("song.mid", 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()

def add_chords(MyMIDI,chords,key):
    for i in range(len(chords)):
        chord = chords[i]
        for note in chord:
            pitch = note + key
            time = i
            MyMIDI.addNote(TRACK,CHANNEL,pitch,time,DURATION,LOW)
    return MyMIDI

def add_notes(MyMIDI,syllables,key,chords):
    note = key%12 + 84
    for i in range(len(chords)):
        syllable = syllables[i]
        chord = chords[i]
        note = generateNextNote(note,'M',key+60)
        print(note)
        if (syllable != 0):
            duration = 1.0 / syllable    
            for j in range(syllable):
                MyMIDI.addNote(TRACK,CHANNEL,note,i+j*duration,duration,HIGH)
    return MyMIDI

# s = [2,1,2,3,2,1,2,3,1,1,2,2,1,1,1,3,2,1,2,3,2,2,2,2,1,1,1,3,2,1,1,2]
# make_song_file(happy1,60,s)
# play_song()