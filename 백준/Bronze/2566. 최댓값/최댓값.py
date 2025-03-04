lt = []

for i in range(9):
    row = list(map(int, input().split()))
    lt.append(row)

lt_max = max(map(max, lt))

for i in range(9):
    if lt_max not in lt[i]:
        pass
    else:
        print(lt_max)
        print(i+1, lt[i].index(lt_max)+1)
        break