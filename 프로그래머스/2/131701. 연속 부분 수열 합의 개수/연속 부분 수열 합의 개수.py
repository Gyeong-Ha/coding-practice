def solution(elements):
    e2 = elements*2
    i = 1 # 합산할 숫자의 개수
    s = set()
    while i < len(elements):
        for e in range(len(elements)):
            subsequence = 0
            subsequence += sum(e2[e:e+i])
            s.add(subsequence)
        i += 1
    answer = len(s) + 1 # 전체 요소의 합은 항상 1가지

    return answer