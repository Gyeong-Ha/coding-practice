lt = []
for i in range(5):
    word = list(input())
    lt.append(word)

answer = ""
for x in range(15):
    y = 0
    while y < 5:
        try:
            answer += lt[y][x]
        except:
            pass
        y += 1
print(answer)