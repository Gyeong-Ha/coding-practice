alphabet_lt = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

S = input()

for letter in alphabet_lt:
    if letter in S:
        print(S.index(letter), end=" ")
    else:
        print(-1, end=" ")