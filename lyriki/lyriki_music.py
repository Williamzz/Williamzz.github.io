import pygame
from midiutil.MidiFile import MIDIFile

TRACK = 0
CHANNEL = 0
DURATION = 1
VOLUME = 100

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

    # tracks are numbered from zero. times are measured in beats.

    track = 0   
    time = 0

    # add track name and tempo.
    MyMIDI.addTrackName(track,time,"Sample Track")
    MyMIDI.addTempo(track,time,100)

    MyMIDI = happy_chords(MyMIDI)

    # and write it to disk.
    binfile = open("song.mid", 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()

def happy_chords(MyMIDI):
    # C F G C chord progression
    c = [60,64,67]
    f = [60,65,69]
    g = [55,62,65]
    chords = [c,c,c,c,f,f,f,f,g,g,g,g,c,c,c,c,f,f,f,f,g,g,g,g,g,g,g,g,c,c,c,c]
    for i in range(len(chords)):
        chord = chords[i]
        for note in chord:
            pitch = note
            time = i
            MyMIDI.addNote(TRACK,CHANNEL,pitch,time,DURATION,VOLUME)
    return MyMIDI

make_song_file(None,None,None)
play_song()