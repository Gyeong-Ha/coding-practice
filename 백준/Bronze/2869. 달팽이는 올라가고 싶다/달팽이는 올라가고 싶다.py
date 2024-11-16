import sys

a, b, v = map(int, sys.stdin.readline().split())

x = (v-b)/(a-b)

if x > int(x):
    x += 1

else:
    x = x

print(int(x))