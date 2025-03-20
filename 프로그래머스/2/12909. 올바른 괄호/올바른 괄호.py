def solution(s):
    answer = True
    s_lt = " ".join(s).split()
    if s_lt.count("(") != s_lt.count(")"):
        answer = False
    l_bracket = 0
    r_bracket = 0
    for i in s:
        if i == "(":
            l_bracket += 1
        elif i == ")":
            r_bracket += 1
        if r_bracket > l_bracket:
            answer = False
            break
    return answer