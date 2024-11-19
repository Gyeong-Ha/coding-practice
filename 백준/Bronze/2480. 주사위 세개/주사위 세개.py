a, b, c = map(int, input().split())
lt = [a, b, c]
s = set(lt)

if len(s) == 1:
    print(10000+a*1000)
elif len(s) == 2:
    for i in lt:
        if lt.count(i) == 2:
            x = i
            break
    print(1000+x*100)
else:
    lt.sort()
    print(lt[2]*100)