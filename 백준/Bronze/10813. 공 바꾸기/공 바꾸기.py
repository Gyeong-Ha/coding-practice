n, m = map(int, input().split())

lt = []
for x in range(1, n+1):
    lt.append(x)

for y in range(m):
    i, j = map(int, input().split())
    backup = lt[i-1]
    lt[i-1] = lt[j-1]
    lt[j-1] = backup

print(" ".join(map(str, lt)))