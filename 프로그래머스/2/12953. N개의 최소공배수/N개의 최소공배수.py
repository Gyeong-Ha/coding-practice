import math

def solution(arr):
    answer = 0
    i = 0
    while len(arr) != 1:
        try:
            update = arr[i] * arr[i+1] // math.gcd(arr.pop(i), arr.pop(i))
            arr.insert(0, update)
        except:
            break
    answer = arr[0]
    return answer