def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        if s == False:
            answer += a * (-1)
        else:
            answer += a
    return answer