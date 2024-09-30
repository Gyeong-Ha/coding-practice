text = input().upper()

# 각 문자 빈도 세기
freq = {}
for letter in text:
    if letter not in freq:
        freq[letter] = 1  # 처음 등장하는 알파벳의 값을 1로 저장
    else:
        freq[letter] += 1 # 재등장하는 알파벳은 기존 값에 +1
max_freq = []
most_key = []
for key, value in freq.items():
    if value == max(freq.values()):
        max_freq.append(value)
        most_key.append(key)
if len(max_freq)>=2:
    print("?")
else:
    print(most_key[0])