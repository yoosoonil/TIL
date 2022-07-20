# 주어진 정수의 각자리수를 더하시오.

# 내 풀이
def solution(n):
    answer=0
    while n>0 :
        answer+=n%10
        n//=10
    return answer

print(solution(123))

# 강사님 풀이
number = 123

# number가 0일 때 Stop!
# => int는 0일 때 False
result = 0
while number:
    # 몫은 다음 number가 됨.
    # 나머지는 더해나가면 된다!
    
    # 1. 
    # answer += number%10
    # number //= 10    

    # 2.
    # divmod(x, y)는 x를 y로 나누고,
    # 결과를 tuple로 반환
    # (몫, 나머지)
    number, remainder = divmod(number, 10)
    result += remainder

print(result)


