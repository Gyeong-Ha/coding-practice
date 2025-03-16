def solution(s):
    answer = ''
    lt = list(map(int, s.split()))
    answer = f"{min(lt)} {max(lt)}"
    return answer