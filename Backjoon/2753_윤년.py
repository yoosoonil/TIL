Y = int(input())

if ((Y % 4 == 0) and (Y % 100 != 0)) or ( Y % 400 == 0):    # '!='은 not이라는 뜻.
    print('1')  # 윤년 조건식이 참인경우
else:
    print('0')  # 거짓인경우