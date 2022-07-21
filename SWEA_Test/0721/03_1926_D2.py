# 숫자만큼 하나씩 뽑을 때 3, 6, 9는 -으로 표시.
# 36은 -- 표시
# 숫자를 문자(str)으로 바꾸고, slicing해서 보기.

N = int(input())
result = ''                             # 값을 모아줄 result 선언

for test_case in range(1, N + 1):       # 넣은 숫자만큼 꺼내기
    num = str(test_case)                # 꺼낸 숫자들을 문자(str)로 변환 why? 숫자내의 숫자를 count 못하니까.
    cnt = 0                             
    
    if '3' in num:                      # num(str)에 3이 있다면
        cnt += num.count('3')           # 3을 카운트해서 cnt에 더함.
    if '6' in num:                          
        cnt += num.count('6')
    if '9' in num:
        cnt += num.count('9')
        
    if(cnt==0):                         # cnt=0 즉, num(str)안에 3, 6, 9가 없다면
        result += num                   # 결과값에 해당 num(str) 추가.
    else:
        for i in range(cnt):            # 앞선 cnt=0이 아니라면, cnt만큼 돌려서 '-' 추가.
            result += '-'
    result += ' '                       # 네번째 if와 else에 대한 값들 추가

print(result)