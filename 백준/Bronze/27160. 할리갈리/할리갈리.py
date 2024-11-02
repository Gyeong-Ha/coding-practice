dic = {"STRAWBERRY": 0, "BANANA": 0, "LIME": 0, "PLUM": 0}

n = int(input())
for i in range(n):
    lt = list(input().split())
    dic[lt[0]] += int(lt[1])

for x in sorted(list(dic.values())):
    if x == 5:
        answer = 1
        break
    else:
        answer = 0

if answer == 1:
    print("YES")
else:
    print("NO")