def solution(n):
    answer = 0
    root = n ** 0.5
    i = 0
    while i < int(root):
        i += 1
        if n % i == 0:
            answer += 1
    answer *= 2
    if int(root)**2 == n:
        answer -= 1
    return answer