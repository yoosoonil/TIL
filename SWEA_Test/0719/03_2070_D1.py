# import sys
# sys.stdin = open("03_2070.txt", "r")

T = int(input())
symbol = ''                             # 부호를 위한 빈칸으로 변수 생성
for i in range(1, T+1):
    a, b = map(int, input().split())
    if a > b:
        symbol = ">"
    elif a == b:
        symbol = "="
    else:
        ""
        symbol = "<"
    print("#{} {}".format(i, symbol))