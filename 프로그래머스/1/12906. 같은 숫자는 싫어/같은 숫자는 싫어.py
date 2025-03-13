def solution(arr):
    answer = []
    s = ""
    for i in arr:
        if i == s:
            pass
        else:
            answer.append(i)
        s = i
    return answer