s = input()
s_set = set()
for i in range(len(s)):
    for j in range(1, len(s)+1):
        s_set.add(s[i:i+j])
print(len(s_set))