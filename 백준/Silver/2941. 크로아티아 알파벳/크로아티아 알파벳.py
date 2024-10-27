word = input()

num = 0
i = 0
croatia_lt = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

while len(word) > 0:
    if word[0:3] in croatia_lt:
        i += 1
        num += 1
        word = word[3:]
    elif word[0:2] in croatia_lt:
        i+=1
        num += 1
        word = word[2:]
    else:
        i+=1
        num += 1
        word = word[1:]

print(num)