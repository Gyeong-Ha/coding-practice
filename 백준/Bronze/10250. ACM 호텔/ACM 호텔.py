T = int(input())

for t in range(T):
    H, W, N = map(int, input().split())

    n = 0
    while True:
        for width in range(1, W+1):
            for height in range(1, H+1):
                if n < N:
                    n += 1
                    h_answer = height
                    w_answer = width
        break
    print(h_answer*100+w_answer)