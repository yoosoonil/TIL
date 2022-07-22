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
    
    k = 0                                   # k의 초기값 //문제 내 kN에서 k를 하나씩 늘려서 곱해야하기에 코드 설정. 
    while(True):
        if 0 in listA:                      # listA 안에 요소 0이 있으면 -> 아래 코드 진행. 
            k += 1                          # k에 반복할 때마다 1 더함.
            num = str(N*k)                  # num은 N*k(1, 2, 3, ...)이다. ex) 1295 * 1, 1295*2, 1295*3 ...
            for j in range(len(num)):       # 1295 -> range(4) -> [0, 1, 2, 3] -> lisA[1], listA[2], listA[9], list[5] 
                listA[int(num[j])] += 1     # listA = [0, 1, 1, 0, 0, 1, 0, 0, 0, 1]  -> 결국 listA의 요소들이 0이 아닐때까지 반복.
        else :                              
            break                           # listA 안에 0이 없으면 -> break.
    print(f'{test_case} {num}')             # #번호와 num 출력
    