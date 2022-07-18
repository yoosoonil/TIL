# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오.
# str 금지.

# 1번째 풀이
def digit_length(n):
    ans = 0

    while n:
        n //= 10        # n 값의 나머지는 버리고, 몫만 남긴다.
        ans += 1        # 그 몫에 1을 더한다.

    return ans          

print(digit_length(123))

# 2번째 풀이
number = 123

cnt = 0

while number:                   # int : 0이 아닌 다른 수면 무조건 True!
# while number != 0:            # 목이 0이 되면 종료해야하니까!
    number //= 10
    cnt += 1
    
print(cnt)