def solution(num):
    i = 0
    while num > 1:
        if num % 2 == 0:
            num = num // 2
            i += 1
        else:
            num = num * 3 + 1
            i += 1
    if num == 1 and i <= 500:
        answer = i
    else:
        answer = -1
    return answer