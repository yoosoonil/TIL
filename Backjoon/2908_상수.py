import sys

sys.stdin = open('2908.txt', 'r')

N = int(input())

for tc in range(1, N + 1):
    a, b = map(int, input().split())
    ra = int(str(a)[::-1])
    rb = int(str(b)[::-1])
    # lst = (ra, rb)
    
    if ra > rb:
        print(ra)
    else:
        print(rb)
    