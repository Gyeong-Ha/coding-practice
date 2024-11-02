dic = {"STRAWBERRY": 0, "BANANA": 0, "LIME": 0, "PLUM": 0}

n = int(input())
for i in range(n):
    lt = list(input().split())
    dic[lt[0]] += int(lt[1])

if 5 in dic.values():
    print('YES')
else:
    print('NO')