# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 적고, 수정하세요.

# 문제 코드
N = 10 
answer = ()
for number in range(N + 1):
    answer.append(number * 2)
    
print(answer)

# 발생오류 : AttributeError: 'tuple' object has no attribute 'append'
# 발생원인 : answer의 소괄호 ( )로 이루어진 튜플은 값 수정이나 삭제, 추가를 할 수 없음. 
# 해결방법 : answer의 소괄호를 대괄호[ ] 로 바꿔 리스트를 만들어야 합니다. 리스트는 값 수정,삭제,추가 가능. 

# 수정 코드
N = 10
answer = []                     #대괄호로 수정
for number in range(N + 1):
    answer.append(number * 2)

print(answer)