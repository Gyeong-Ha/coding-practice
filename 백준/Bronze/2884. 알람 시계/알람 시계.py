h, m = map(int, input().split())

if m >= 45:
    changed_m = m - 45
    changed_h = h
else:
    changed_m = m - 45 + 60
    changed_h = h - 1

if h == 0 and m < 45:
    changed_h = 23

print(changed_h, changed_m)