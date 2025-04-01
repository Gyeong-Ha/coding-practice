def solution(s):
    answer = []
    del_zero = 0
    i = 0

    while True:
        if s == "1":
            answer = [i, del_zero]
            break
            
        # 0 개수 세서 del_zero에 저장 후 s에서 제거하기
        del_zero += s.count('0')

        # 0 제거
        s = s.replace('0', '')

        # s의 길이 c를 이진변환해서 s로 저장
        c = len(s)
        s = bin(c)
        s = s[2:]

        # 횟수 i 업뎃
        i += 1
        
    return answer