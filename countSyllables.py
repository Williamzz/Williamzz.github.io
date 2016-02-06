
# reduces common combinations of vowels of one syllable
def reduceIrregulars(word, length):
    totalReduce = 0
    truncateList = ["ya", "yo", "oa", "ea", "ee", "oo", "ui", "au", "ou", 
    "oi", "eu", "iou", "you"]
    for i in range(len(word)):
        if word[i:i+length] in truncateList:
            totalReduce += 1
    return totalReduce

def countSyllables(word):
    word = word.lower()
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
    if word[-2:-3] in ["ie"]:
        count -= 1
    if word.endswith("e"):
        if word[-3] in ["a", "e", "i", "o", "u", "n", "l"]:
            count -= 1
    return count

# words with "ue" in them (e.g. True, Fatigue) tend to act weird
