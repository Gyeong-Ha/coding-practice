def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for _ in range(len(A)):
        answer += A.pop() * B.pop()
    return answer