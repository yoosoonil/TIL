import sys

sys.stdin = open('02_1976.txt', "r")

# 입력된 값은 시와 분.
# 각 시간의 합을 구해서 시 분으로 표시
# 단, 시는 1-12, 분은 0-60으로 표시

T = int(input())                            # test_case에 필요한 숫자

hr = 0
minn = 0

for test_case in range (1, T + 1):
    numbers = list(map(int, input().split()))       # 시 분을 공백줘서 넣어줄거니까. split씀. 숫자이기에 int쓰고싶어 map씀
    hr = numbers[0] + numbers[2]                    # ex) 3 17 1 39 -> list -> [3, 17, 1, 39]        
    minn = numbers[1] + numbers[3]                  #                           0  1   2  3
    if hr > 12 :
        hr -= 12
    if minn >= 60 :
        minn -= 60
    print(f'{test_case} {hr} {minn}')