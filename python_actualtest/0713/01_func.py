# 숫자 n을 받아 (Input)
# 세제곱 결과를 반환하는 (Output)
# 함수 cube를 정의하시오. 
# cube 함수를 호출하여 12의 세제곱 결과를 출력하시오.

# Output = 1728

num = int(input())      # num에 숫자를 입력하기. terminal창에서 12입력.
def cube(n):            # cube 함수(세제곱) 선엉
    return n * n * n    # n**3 <- 제곱근식
 
result = cube(num)      # 결과값으로 cube 함수 불러오기
print(result)
