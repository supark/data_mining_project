from collections import Counter
import re

def openfile(filename):
    ft = open(filename, "r+")
    str = ft.read()
    ft.close()
    return str

def removegarbage(str):
    str = re.sub(r'\W', ' ', str)
    str = str.lower()
    return str

def getwordbins(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt

def main(filename, topwords):
    txt = openfile(filename)
    txt = removegarbage(txt)
    words = txt.split(' ')
    bins = getwordbins(words)
    for key, value in bins.most_common(topwords):
        print (key, value)

main("./extractText.json", 500)
