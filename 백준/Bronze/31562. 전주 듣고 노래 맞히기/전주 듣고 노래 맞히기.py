import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())

dic = {}
for i in range(n):
    t, s, a1, a2, a3, a4, a5, a6, a7 = input().split()
    dic[s] = f"{a1} {a2} {a3}"

for j in range(m):
    str = input()
    x = Counter(dic.values())[str]
    if x == 0:
        print("!")
    elif x == 1:
        dicReversedKV = {v:k for k,v in dic.items()}
        print(dicReversedKV.get(str))
    else:
        print("?")