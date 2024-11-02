import sys
t = int(sys.stdin.readline())
s = {}
for i in range(t):
    name, enter_or_leave = input().split()
    if enter_or_leave == "enter":
        s[name] = 1
    else:
        del s[name]
s = sorted(s.keys(), reverse=True)
for person in s:
    print(person)