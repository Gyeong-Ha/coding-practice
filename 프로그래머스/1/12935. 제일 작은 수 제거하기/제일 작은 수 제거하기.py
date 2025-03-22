def solution(arr):
    arr.remove(min(arr))
    answer = arr
    if answer == []:
        answer = [-1]
    return answer