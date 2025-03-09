t = int(input())
for i in range(t):
    cash = int(input())
    q = cash // 25
    cash %= 25
    d = cash // 10
    cash %= 10
    n = cash // 5
    cash %= 5
    p = cash // 1
    print(q, d, n, p)