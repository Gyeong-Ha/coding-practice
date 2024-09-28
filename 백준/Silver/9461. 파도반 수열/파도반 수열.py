T = int(input())
for t in range(T):
    N = int(input())
    a = 1
    b = 1
    c = 1
    if N <= 3:
        print(1)
    else:
        for num in range(1, N+1):
            if num <= 3:
                pass
            else:
                k = a + b
                a = b
                b = c
                c = k
        print(k)