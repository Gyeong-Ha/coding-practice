def solution(s):
    s = s.lower()
    p_num = s.count('p')
    y_num = s.count('y')
    if p_num == 0 and y_num == 0:
        answer = True
    elif p_num == y_num:
        answer = True
    elif p_num != y_num:
        answer = False
    return answer