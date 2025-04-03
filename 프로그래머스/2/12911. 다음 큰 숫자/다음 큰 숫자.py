def solution(n):
    m = n + 1
    binary_n = str(bin(n)).count('1')
    while True:
        if binary_n == str(bin(m)[2:]).count('1'):
            answer = m
            break
        m += 1
    return answer