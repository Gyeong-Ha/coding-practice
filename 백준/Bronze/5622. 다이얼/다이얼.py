dic = {
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"]
}

word = input()

answer = 0
for idx in range(len(word)):
    lt = [k for k, v in dic.items() if word[idx] in v]
    answer += lt[0] + 1

print(answer)