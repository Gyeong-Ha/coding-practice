n = int(input())

lt = list(map(int, input().split()))

m = max(lt)

alter_lt = []

for score in lt:
    alter_lt.append(score/m*100)

print(sum(alter_lt)/len(alter_lt))