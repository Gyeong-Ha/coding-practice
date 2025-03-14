from collections import Counter

def solution(participant, completion):
    try:
        answer = list(set(participant) - set(completion))
        answer = answer[0]
    except:
        participant.sort()
        answer = Counter(participant) - Counter(completion)
        answer = list(Counter.keys(answer))
        answer = answer[0]
    return answer