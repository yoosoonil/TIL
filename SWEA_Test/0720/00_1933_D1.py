# 주어진 수의 약수를 구하고 약수를 오름차순으로 정렬한다.

N = int(input())
for i in range(1, N + 1):
    if N % i == 0:
        # 만족한다면 약수
        print(i, end = ' ')
print()