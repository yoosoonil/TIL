# 문제 코드
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)

# 발생오류 : 값이 5.5로 나와야하는데, 55 나옴.
# 발생원인 : count의 들여쓰기 문제와 total 식 수정 필요.
# 해결방법 : count 들여써주고, //은 몫연산이므로 /(나눗셈) 연산으로 수정.

# 수정 코드
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)

