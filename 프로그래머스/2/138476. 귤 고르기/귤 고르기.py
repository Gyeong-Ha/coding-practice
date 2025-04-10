from collections import Counter

def solution(k, tangerine):
    answer = 0
    i = 0
    num = 0
    counter = list(Counter(tangerine).values())
    counter.sort(reverse=True)
    while num < k:
        num += counter[i]
        answer += 1
        i += 1
    return answer