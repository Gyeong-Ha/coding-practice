import sys

n, m = map(int, sys.stdin.readline().split())

dic = {}
for i in range(1, n+1):
    s = sys.stdin.readline()[:-1]
    dic[s] = i
    dic[i] = s

for j in range(m):
    x = sys.stdin.readline()[:-1]
    try:
        x = int(x)
        print(dic[x])
    except:
        print(dic[x])