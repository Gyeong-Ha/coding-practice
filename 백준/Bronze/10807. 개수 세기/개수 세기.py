n = int(input())

lt = []
num_str = input()
num_lt = num_str.split(" ")
x = int(input())

answer = 0
for i in num_lt:
    if int(i) == x:
        answer += 1

print(answer)