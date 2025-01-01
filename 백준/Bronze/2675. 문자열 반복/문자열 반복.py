T = int(input())

for t in range(T):
    R, S = input().split()
    P = ""
    for idx in range(len(S)):
        P += S[idx]*int(R)
    print(P)