def solution(n):
    x =  n ** 0.5
    if x == int(x):
        answer = (x+1)**2
    else:
        answer = -1
    return answer