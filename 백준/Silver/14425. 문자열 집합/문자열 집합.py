from collections import Counter

n, m = map(int, input().split())

s = list()
for i in range(n):
    s_element = input()
    s.append(s_element)
s = Counter(s)

answer = 0
for i in range(m):
    x = input()
    if x in s:
        answer += Counter(s)[x]
print(answer)