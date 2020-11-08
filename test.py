import random
import fileinput
import os
import random

def dictinize(filename_text):
    d = {}
    with open(filename_text) as f:
        for line in f:
            (key, val) = line.split(" ",1)
            d[int(key)] = val
    return d

survPerks = dictinize("survivorperks.txt")
killerPerks = dictinize("killerperks.txt")
filename = 'characters.txt'

def random_line():
    line_num = 0
    selected_line = ''
    with open(filename, encoding="utf8") as f:
        while 1:
            line = f.readline()
            if not line: break
            line_num += 1
            if random.uniform(0, line_num) < 1:
                selected_line = line
    return selected_line.strip()


def randomPerks(referredDictionary):
    numb = 0
    arrayOfUsedNumbers = []
    listOfPerks = []
    while numb != 4:
        randNumb = random.randint(1, len(referredDictionary))
        if randNumb in arrayOfUsedNumbers:
            continue
        else:
            arrayOfUsedNumbers.append(randNumb)
            listOfPerks.append(referredDictionary.get(randNumb))
            numb = numb + 1
    return listOfPerks

listOfPerks = randomPerks(killerPerks)
helpPage = open('help.txt', 'r').read()
print(helpPage)
print ("These perks: " + listOfPerks[0] + ", " + listOfPerks[1] + ", " + listOfPerks[2] + " and " + listOfPerks[3])