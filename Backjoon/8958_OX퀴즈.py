import sys
from tabnanny import check

sys.stdin = open('8958.txt', 'r')

N = int(input())

for tc in range(1, N + 1):
    check = input()             # 'OOXXOXXOOO' 문자열 입력
    check_list = list(check)         # 문자열을 하나씩 요소로 list화
    total = 0                    
    cnt = 1                     # 연속적인 문자에 대해 숫자를 더해주기위해 cnt=1로 설정.
    for i in check_list:        # [O, O, X, X, O, X, X, O, O, O]에서 하나씩 꺼냄.
        if i == 'O':            # 꺼낸 요소가 O라면    
            total += cnt        # total에 cnt를 더해주고 cnt에 1씩 더함으로서 연속적인 문자에 대해 1씩 더하게 됨.
            cnt += 1            
        else:                   # 0가 아니라면 cnt=1로 다시 초기화.
            cnt = 1
    print(total)