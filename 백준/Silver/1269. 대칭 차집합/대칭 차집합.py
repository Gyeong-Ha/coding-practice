import sys

input = sys.stdin.readline

a_num, b_num = map(int, input().split())

a_set = set(input().split())
b_set = set(input().split())

print(len(a_set-b_set)+len(b_set-a_set))