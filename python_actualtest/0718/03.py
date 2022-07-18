# 두 수를 input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

#문제 코드
numbers = input().split()
print(sum(numbers))

# 발생오류 : TypeError: unsupported operand type(s) for +: 'int' and 'type'
# 발생원인 : input에 처음들어간 값은 int이지만, 뒤에 들어가는 값이 str이기에 숫자+문자열로 덧셈함수가 작용 x
# 해결방법 : map함수를 사용해서 입력되는 값을 int로 바꿔주게끔 한다.

# 수정 코드
numbers = input().split()
result = sum(map(int, numbers))
print(result)


