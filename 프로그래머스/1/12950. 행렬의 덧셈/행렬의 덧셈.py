def solution(arr1, arr2):
    answer = []
    col = len(arr1[0])
    row = len(arr1)
    for r in range(row):
        e = []
        for c in range(col):
            e.append(arr1[r][c]+arr2[r][c])
        answer.append(e)
    return answer