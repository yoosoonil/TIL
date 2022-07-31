N = int(input())

if N == 1:
    print('*')
    
else:
    for n in range(N):
        if n % 2 == 0:              # 짝수라면 *띄어쓰기로 곱하는구나~!
            a = print('* ' * N)
        else:
            b = print(' *' * N)     # 홀수라면 띄어쓰기*를 곱하는 것.