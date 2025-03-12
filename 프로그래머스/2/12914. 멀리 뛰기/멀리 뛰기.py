import math

def solution(n):
    answer = 1
    two_num = n // 2
    one_num = (n - two_num) // 1
    
    for two in range(1, two_num+1):
        one = n - 2 * two
        outcomes = math.factorial(two+one) // (math.factorial(two) * math.factorial(one))
        answer += outcomes
    answer = answer % 1234567
    return answer