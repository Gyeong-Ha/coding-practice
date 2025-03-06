# 2차원 배열 생성
lt = []
for i in range(100):
    lt.append([])
    for j in range(100):
        lt[i].append(0)

# 입력값에 따라 2차원 배열에 1 배치
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for x_fill in range(x, x+10):
        for y_fill in range(y, y+10):
            lt[x_fill][y_fill] = 1

# 1의 개수만 세기
answer = 0
for i in lt:
    answer += i.count(1)
print(answer)