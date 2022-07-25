import sys

sys.stdin = open('10953.txt', "r")

N = int(input())

for test_case in range(1, N + 1):
    a, b = map(int, input().split(','))
    print(a + b)