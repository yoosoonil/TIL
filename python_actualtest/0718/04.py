# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 문제 코드
words = list(map(int, input().split()))
print(words)

# 발생오류 : ValueError: invalid literal for int() with base 10: "I'm"
# 발생원인 : 문자열(string)을 받는 것
# 해결방법 : '6'도 문자열로 변환해줘야한다. int -> str로 수정한다.

# 수정 코드
words = list(map(str, input().split()))
print(words)
