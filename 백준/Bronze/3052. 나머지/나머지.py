lt = []

for i in range(10):
    n = int(input())
    if n % 42 not in lt:
        lt.append(n%42)

print(len(lt))