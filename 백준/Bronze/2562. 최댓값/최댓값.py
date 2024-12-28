lt = [0]
for i in range(9):
    x = int(input())
    if lt[0] < x:
        del lt[0]
        lt.append(x)
        answer_i = i+1
print(lt[0])
print(answer_i)