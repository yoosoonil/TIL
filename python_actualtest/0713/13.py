# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

# Input = apple
# Output = elppa

# word = 'apple'
# re_word = word[::-1]
# print(re_word)

# 관련 개념 url
# https://itholic.github.io/python-reverse-string/

s = 'apple'
s_reverse = ''  # 기존 문자열을 역순으로 담아줄 빈 문자열 선언
for char in s:
    s_reverse = char + s_reverse

print(s_reverse)  # edcba

word = 'apple'

for i in range(len(word)):
    print(word)