lt = [x for x in range(1, 31)]

for i in range(28):
    num = int(input())
    lt.remove(num)

lt.sort()

print(lt[0])
print(lt[1])