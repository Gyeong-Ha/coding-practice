n, m = map(int, input().split())

dic = {}
for x in range(1, n+1):
    dic[x] = 0

for y in range(m):
    i, j, k = map(int, input().split())
    for i_to_j in range(i, j+1):
        dic[i_to_j] = k

for v in dic.values():
    print(v, end=" ")