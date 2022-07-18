# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 문제 코드
numbers = 22020718
print(len(numbers))

# 발생오류 : TypeError: object of type 'int' has no len()
# 발생원인 : len 함수는 문자열의 길이만 측정하기에 숫자에 적용할 수 없다.
# 해결방법 : 어쩔 수 없이 숫자를 문자열로 바꿔줄 수 밖에 없다. 따옴표를 찍든가 str로 변형해주자.

# 수정 코드
numbers = '22020718' # or str(22020718)
print(len(numbers))  # or print(len(str(numbers)))