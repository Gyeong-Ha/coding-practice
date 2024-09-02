def solution(x):
    n = 0
    for i in range(len(str(x))):
        n += int(str(x)[i])
    if x % n == 0:
        answer = True
    else:
        answer = False
    return answer