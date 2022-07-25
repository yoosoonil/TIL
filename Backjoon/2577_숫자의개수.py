a = int(input())
b = int(input())
c = int(input())

mtp = a * b * c

result = [0]*10
# result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

num = str(mtp)
for i in range(len(num)):
    # 17037300 -> 8자리수 -> 요소 0-7까지 숫자를 넣음.
    result[int(num[i])] += 1
    

print(*result, sep = '\n')
# Unpacking Operator * 를 사용하여 리스트를 구분자를 넣어 바로 출력하는 방법이다.

     