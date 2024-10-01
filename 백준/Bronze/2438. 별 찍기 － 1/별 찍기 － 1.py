n = int(input())

i = 1
while n != 0:
    print("*"*(i))
    i += 1
    n -= 1
    if n == 0:
        break