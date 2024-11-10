from collections import Counter

def main():
    filepath = "books/frankenstein.txt"
    text = getBookText(filepath)
    charDict = getCharCount(text)
    charReport(charDict)


def getBookText(file):
    with open(file) as f:
        return f.read()


def getCharCount(text):
    '''charDict = {}
    for char in text:
        lowered = char.lower()
        if lowered in charDict:
            charDict[lowered] += 1
        else:
            charDict[lowered] = 1
    '''
    charDict = Counter(text.lower())
    return charDict

def charReport(charDict):
    charDictSorted = dict(sorted(charDict.items()))

    for char in charDictSorted:
        letter = char
        count = charDict[char]

        print("The", char," character was found ", count, "times")

main()