import sys

sys.stdin = open('01_1989.txt', "r")

# 거꾸로 읽는 코드쓰기.
# input과 거꾸로 출력한 것이 맞으면 1
# 아니면 0

T = int(input())                            # test_case에 필요한 숫자

for test_case in range (1, T + 1):          
    word = input('')                        # word 정의
    
    r_word = word[::-1]                     # r_word 정의
    temp = ''                               # word에서 뽑아서 나온 문자를 다시 문자열로 복구하기위한 리스트 정의
    for i in range(len(word)):              # word의 문자열 길이만큼 뽑아 씀.
        temp += word[i]                     # temp에 문자열 합쳐주는 코드
        
        if temp == r_word:                  # word와 r_word의 조건문.
            result = 1
        else:
            result = 0
    print(f'#{test_case} {result}')         # 출력 코드.