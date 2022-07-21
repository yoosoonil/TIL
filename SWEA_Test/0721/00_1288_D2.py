import sys

sys.stdin = open('00_1288.txt', "r")

# N번째 양
# 2N, 3N, 4N ....
# N번째 양의 숫자를 나열하고
# 그 숫자들이 0-9까지 다 나열된다면
# 멈춘다.
# 1 =< N =< 10**6

# 필요코드
# N에 1, 2, 3,... 곱해줄 코드.
# 1, 2, 3, 4... 무한정 늘어나는 수.
# 그 곱해진 숫자를 list할 코드
# list해서 나온 숫자들이 0-9나오면 멈춰줄 코드

T = int(input())                            # test_case에 필요한 숫자

for test_case in range (1, T + 1):          # test_case 돌리는 코드.
    N = int(input())                        # input값 설정
    
    listA = [0]*10                          # listA -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    i = 0                                   # i의 초기값
    while(True):
        if 0 in listA:                      # listA 안에 0없으면 -> break 즉, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]되면 break
            i += 1                          # i에 1씩 더함.
            num = str(N*i)                  # num은 N*i(1, 2, 3, ...)이다. ex) 1295 * 1
            for j in range(len(num)):       # 1295 -> range(4) -> [0, 1, 2, 3] -> lisA[1], listA[2], listA[9], list[5] 
                listA[int(num[j])] += 1     # listA = [0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
        else :                              # listA 안에 0이 없으면 -> break.
            break                            
    print(f'{test_case} {num}')             # 번호와 num 출력
    