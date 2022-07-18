# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

# Input 
# apple

# Output
# pple

# 아래는 단어를 입력하여 출력하는 방법
# word = input()
# re_word = ''
# for i in word:
#     if i != 'a':
#         re_word += i
# print(re_word)

# 단어를 직접넣고 출력하는 법.
word = 'apple'
re_word = ''
for i in word:
    if i != 'a':
        re_word += i
print(re_word)

# word = 'apple'
# #반복! for
# for char in 'apple':
#     # 만약 a 일때
#     if char == 'a':
#         print(char)
#         # 반복문에서 아무것도 안하고 넘어가는?
#         # continue
        