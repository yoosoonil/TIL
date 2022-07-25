import sys

sys.stdin = open('10950.txt', "r")

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print(a + b)