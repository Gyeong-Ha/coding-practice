n = int(input())

lt = list(map(int, input().split()))
lt.sort()

print(lt[0], lt[-1])