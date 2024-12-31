n, m = map(int, input().split())

lt = [str(x) for x in range(1, n+1)]

for x in range(m):
    i, j = map(int, input().split())
    idx = 0
    for alter in reversed(lt[i-1:j]):
        lt[i-1+idx] = alter
        idx += 1

print(" ".join(lt))