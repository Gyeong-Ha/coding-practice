h, m = map(int, input().split())
time = int(input())

hm = h*60+m
hm += time

while hm >= 1440:
    hm -= 1440

h = hm // 60
m = hm % 60
print(h, m)