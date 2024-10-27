from itertools import groupby

def findContLetter(s):
    dic = {}
    for letter, contLetter in groupby(s):
        if letter not in dic:
            dic[letter]=list(contLetter)
        else:
            dic["iter"]="iter"
    return dic

t = int(input())
num = 0
for i in range(t):
    word = input()
    if "iter" not in findContLetter(word):
        num += 1

print(num)