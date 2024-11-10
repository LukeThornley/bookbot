def main():
    filepath = "books/frankenstein.txt"
    text = getBookText(filepath)
    wordCount = getWordCount(text)
    print(wordCount)

def getBookText(file):
    with open(file) as f:
        return f.read()

def getWordCount(text):
    wordCount = len(text.split())
    return wordCount

main()