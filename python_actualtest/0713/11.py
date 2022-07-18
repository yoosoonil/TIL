# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

numbers = list(range(1,10))

for i in numbers :
    if i == 1 :
        continue # continue 코드는 실행하지않고 건너 뜀.
    print(i,'단',sep='')
    for j in numbers :
        print(i, 'x', j, '=', i*j)