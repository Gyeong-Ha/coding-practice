def solution(brown, yellow):
    answer = []

    x = brown // 2
    h = 3
    v = 1

    while x != h+v:
        h += 1
        if x == h+v:
            break
        else:
            v += 1
    
    while yellow != (h-2)*(v):
        h += 1
        v -= 1
        
    answer.append(h)
    answer.append(v+2)
    
    return answer