import random

with open("book.txt", "r", encoding="utf-8") as bookFile:
    text = bookFile.read()

text = text.lower()
text = text.split()
setOfList = {}
for i in range(len(text) - 1):
    word = text[i]
    nextWord = text[i + 1]
    if word not in setOfList:
        setOfList[word] = [nextWord]
    else:
        setOfList[word].append(nextWord)

currentWord = random.choice(list(setOfList.keys()))
print(currentWord)

for i in range(200):
    nextWord = random.choice(setOfList[currentWord])
    if nextWord in list(setOfList.keys()):
        print(f'{i + 1} => {nextWord}')
        # print(nextWord, end=' ')
        currentWord = nextWord
