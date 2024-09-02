def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)):
        answer.append(n[i])
    answer.sort(reverse=True)
    answer = int(''.join(answer))
    return answer