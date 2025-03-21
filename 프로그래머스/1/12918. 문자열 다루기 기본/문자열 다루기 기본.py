def solution(s):
    answer = False
    try:
        int(s)
        if len(s) == 4 or len(s) == 6:
            answer = True
    except:
        pass
    return answer