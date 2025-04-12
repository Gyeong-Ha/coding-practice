def cal(x):
    if x % 2 == 0:
        return x // 2
    else:
        return (x+1)//2

def solution(n,a,b):
    round = 1
    a, b = cal(min(a, b)), cal(max(a, b))
    while True:
        if a == b:
            break
        else:
            a = cal(a)
            b = cal(b)
        round += 1
    answer = round    
    return answer