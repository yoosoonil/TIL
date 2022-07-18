# 문제 코드
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1

print(count)

# 발생오류 : 답인 3이 안나오고 12가 나옴.
# 발생원인 : 조건문이 계속 True 이기에 HappyHacking 전체글자 수인 12가 나옴.
# 해결방법 : aeiou만 조건이 되게 수정.

# 수정 코드
# 1번째 풀이코드
word = "HappyHacking"

vowel = ['a', 'e', 'i', 'o', 'u']

count = 0

for char in word:
    count += vowel.count(char)
        
print(count)

# 2번째 풀이코드
word = "HappyHacking"

count = 0

for char in word:
    if char in 'aeiou':
        count += 1

print(count)

