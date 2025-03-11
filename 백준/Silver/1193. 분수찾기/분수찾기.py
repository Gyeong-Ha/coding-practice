x = int(input())
diag = 1

while x > diag * (diag + 1) // 2:
    diag += 1

prev_total = (diag - 1) * diag // 2

offset = x - prev_total

if diag % 2 == 0:
    numerator = offset
    denominator = diag + 1 - offset
else:
    numerator = diag + 1 - offset
    denominator = offset

print(f"{numerator}/{denominator}")