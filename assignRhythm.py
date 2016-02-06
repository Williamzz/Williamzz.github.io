import string

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
    lines = lyrics.splitlines()
    for line in lines:
        lyricSyllables += lineSyllables(line)[0]
    return lyricSyllables

##############################################################
####    0 ----> new lines                               ######
####    1 ----> quarter                                 ######
####    2 ----> two eighths                             ######
####    3 ----> triplets                                ######
####    4 ----> double two eights or triplet + quarter  ######
####    etc...                                          ######
##############################################################

def assignRhythm(lyrics):
    beats = []
    lines = lyrics.splitlines()
    for line in lines:
        beats += lineSyllables(line)[1:]
        beats += [0]
    return beats

