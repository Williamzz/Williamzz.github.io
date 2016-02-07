import string
import copy

# reduces common combinations of vowels of one syllable
def onlyLetters(s):
    result = ""
    for c in s:
        if c in string.ascii_lowercase:
            result += c
    return result

def reduceIrregulars(word, length):
    totalReduce = 0
    truncateList = ["ya", "yo", "ay", "oa", "ea", "ee", "oo", "ui", 
    "au", "ou", "ie", "oi", "eu", "io", "iou"]
    for i in range(len(word)):
        if word[i:i+length] in truncateList:
            totalReduce += 1
    return totalReduce

# words with "ue" in them (e.g. True, Fatigue) tend to act weird
def syllableCount(word):
    word = word.lower()
    word = onlyLetters(word)
    count = 0
    for letter in word:
        if letter in ["a", "e", "i", "o", "u", "y"]:
            count += 1
    # set to count+1 for words with many vowels
    for i in range(2, count+1):
        count -= reduceIrregulars(word, i)
    for outliers in ["es", "ed"]:
        if word.endswith(outliers):
            count -= 1
    if word.endswith("e") and len(word)>2:
        if word[-3] in ["a", "e", "i", "o", "u", "n", "l"]:
            count -= 1
    if word.endswith("asses"):
        count += 1
    if count == 0:
        count += 1
    return count

# for facebook, the line is split by post or by periods (.)
def lineSyllables(line):
    wordList = []
    lineTotal = 0
    for word in line.split(" "):
        if word in string.whitespace: continue
        wordList.append(syllableCount(word))
        lineTotal += syllableCount(word)
    return [lineTotal] + wordList

def totalSyllables(lyrics):
    lyricSyllables = 0
    lines = lyrics.split("/")
    for line in lines:
        lyricSyllables += lineSyllables(line)[0]
    return lyricSyllables

def assignRhythm(lyrics):
    beats = []
    lines = lyrics.split("/")
    for line in lines:
        beats += lineSyllables(line)[1:]
        beats += [0]
    return beats

##############################################################
####    0 ----> new lines                               ######
####    1 ----> quarter                                 ######
####    2 ----> two eighths                             ######
####    3 ----> triplets                                ######
####    4 ----> double two eights or triplet + quarter  ######
####    etc...                                          ######
##############################################################

# returns list with 32 ints each representing a quarter beat in a measure
def lyricsModification(lyrics):
    rhythm = copy.copy(assignRhythm(lyrics))
    zeroInsert = 3
    while len(rhythm) < 32:
        index = 0
        copyRhythm = copy.copy(rhythm)
        for i in copyRhythm:
            index += 1
            if len(rhythm) == 32:
                break
            elif i == 6:
                rhythm.remove(i)
                rhythm.insert(index, 3)
                rhythm.insert(index, 3)
            elif i == 5:
                rhythm.remove(i)
                rhythm.insert(index, 3)
                rhythm.insert(index, 2)
            elif i == 4:
                rhythm.remove(i)
                rhythm.insert(index, 2)
                rhythm.insert(index, 2)
        if len(rhythm) == 32:
            break
        else: 
            rhythm += [0]

    return rhythm

def run(lyrics):
    if (len(assignRhythm(lyrics)) > 32):
        print ("your creation is %d words too long!" % (len(assignRhythm(lyrics))-32))
        return None
    else: 
        return lyricsModification(lyrics)








