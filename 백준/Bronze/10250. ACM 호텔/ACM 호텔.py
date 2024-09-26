T = int(input())
for t in range(0, T):
    i = 0
    H, W, N = map(int, input().split())
    for w in range(1, W+1):
        for h in range(1, H+1):
            i += 1
            if i == N:
                answer = h*100 + w
                print(answer)
                continue
            else:
                pass