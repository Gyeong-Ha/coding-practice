n, x = map(int, input().split())
str = input()
lt = str.split(" ")

answer = ""
for i in lt:
    if int(i) < x:
        answer += i + " "

print(answer.rstrip())