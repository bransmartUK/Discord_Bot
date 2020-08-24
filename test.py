import random
import fileinput
import os

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


print (random_line())