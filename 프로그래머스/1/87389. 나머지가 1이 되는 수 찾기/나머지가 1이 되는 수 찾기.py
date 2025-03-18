def solution(n):
    answer = n - 1
    if (n - 1) % 2 == 0:
        answer = 2
    else:
        root = int(n ** 0.5)
        for i in range(3, root+1):
            if (n - 1) % i == 0:
                answer = i
                break
    return answer