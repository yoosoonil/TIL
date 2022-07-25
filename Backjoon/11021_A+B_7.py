import sys

sys.stdin = open('11021.txt', 'r')

N = int(input())

for test_case in range(1, N + 1):
    a, b = map(int, input().split())
    c = a + b
    print(f'Case #{test_case}: {c}')