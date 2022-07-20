# 주어진 수를 거꾸로 출력하시오.

Number=1234
Reverse = 0

while(Number > 0):
    Reminder = Number % 10                # 10으로 나누고 몫을 구하는 것.
    Reverse = (Reverse *10) + Reminder
    Number = Number //10

print(Reverse)


# 강사님 풀이
# 1
number = 123

print(int(str(number)[::-1]))

# 3
result = 0
while number:
    # 이전 결과에 10을 곱하고
    result *= 10
    # 나머지를 더해주고
    result += number%10
    # number를 깎는다.
    number //= 10

print(result)