# python 연습장.py < input.txt

import sys

input = sys.stdin.read

def main():
    data = input().splitlines() # 각 라인이 리스트의 한 요소로 저장된다

    # 한 줄(시간대별)씩 리스트 만들어 2중 리스트 생성
    # 이름 추출, 딕셔너리의 키로 사용
    lt = []
    lt_2 = []
    for time in data[1:]:
        lt.append(time.split())
        lt_2 += time.split()
    s = set(lt_2)
    s.discard('-')
    dic = {}
    for element in s:
        dic[element] = 0

    # 시간대별로 분리한 리스트 상에서 짝수 인덱스는 항상 4 추가, 홀수 인덱스는 6과 10 번갈아가며 추가
    kluge = 0
    for j in range(len(lt)):
        if j % 2 == 0:
            for x in lt[j]:
                if x != '-':
                    dic[x] += 4
        else:
            if kluge == 0:
                for x in lt[j]:
                    if x != '-':
                        dic[x] += 6
                kluge = 1
            elif kluge == 1:
                for x in lt[j]:
                    if x != '-':
                        dic[x] += 10
                kluge = 0

    # 딕셔너리의 밸류간 차이 구하기 - 가장 작은 수와 큰 수의 차만 알면 된다!
    # 12 이하면 "Yes", 초과하면 "No"
    if dic and max(dic.values()) - min(dic.values()) > 12:
        sys.stdout.write("No")
    else:
        sys.stdout.write("Yes")

if __name__ == "__main__":
    main()
