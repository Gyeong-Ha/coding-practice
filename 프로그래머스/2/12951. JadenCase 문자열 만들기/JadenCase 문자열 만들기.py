def solution(s):
    answer = ''
    s_lt = s.replace(' ', ' * ').split()
    for e in s_lt:
        if e == '*':
            answer += ' '
        else:
            try:
                int(e[0])
                answer += e.lower()
            except:
                answer += e[0].upper() + e[1:].lower()
    return answer