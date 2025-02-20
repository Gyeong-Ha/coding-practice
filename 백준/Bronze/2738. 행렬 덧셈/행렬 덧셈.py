N, M = map(int, input().split())
a = []
b = []
for n in range(N):
    a_element_lt = list(map(int, input().split()))
    a.append(a_element_lt)
for n in range(N):
    b_element_lt = list(map(int, input().split()))
    b.append(b_element_lt)

for i in range(N):
    lt = []
    for j in range(M):
        lt.append(str(a[i][j]+b[i][j]))
    print(' '.join(lt))