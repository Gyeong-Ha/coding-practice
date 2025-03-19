def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        idx = len(s) // 2 - 1
        answer = s[idx:idx+2]
    else:
        idx = (len(s) - 1) // 2
        answer = s[idx]
    return answer