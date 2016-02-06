import random

def chordType(chord):
    if chord == "m":
        return [ -12, -9, -5, 0, 3, 7, 12]
    elif chord == "M7":
        return [ -12, -8, -5, -1, 0, 4, 7, 11, 12]
    else:
        return [ -12, -8, -5, 0, 4, 7, 12]

# enters int
def compatibleNotesToChord(key, chord):
    scales = chordType(chord)
    for i in range(len(scales)):
        scales[i] += key
    return scales

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