def solution(n):
    answer = 0
    for i in range(1, n+1):
        x = 0
        while x <= n:
            x += i
            i += 1
            if x == n:
                answer += 1
            elif x > n:
                break
            else:
                pass
    return answer