def solution(n):
    answer = 0
    for i in range(1, int(n**0.5)+1):
        if n % 1 == 0 and float(i) != n**0.5 and i*(n//i)==n:
            answer += i + (n//i)
        elif n % i == 0 and float(i) == n**0.5:
            answer += i
        else:
            pass
    return answer