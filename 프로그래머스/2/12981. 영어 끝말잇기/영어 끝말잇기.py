def solution(n, words):
    answer = []
    compare = [words[0]]
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in compare:
            if (i+1)%n == 0:
                player = n
            else:
                player = (i+1)%n
            round = (i+1-player)//n+1
            answer = [player, round]
            break
        else:
            compare.append(words[i])
    if answer == []:
        answer = [0, 0]
    return answer