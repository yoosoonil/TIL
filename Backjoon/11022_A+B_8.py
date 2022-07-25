import sys

sys.stdin = open('11022.txt', 'r')

N = int(input())

for tc in range(1, N + 1):
    a, b = map(int, input().split())
    c = a + b
    print(f'Case #{tc}: {a} + {b} = {c}')
    
    #"Case #x: A + B = C"