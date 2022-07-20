import sys

sys.stdin = open('0720/03_1986.txt', "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    s = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            s = s - i
        else:
            s = s + i
                    
    print(f'#{t}', s)
        
        

# k = int(input())

# for i in range(1, k+1):
#     n = int(input())
#     sum = 0
#     for j in range(1, n+1):
#         if j % 2== 0:
#             sum = sum - j
#         else:
#             sum = sum + j
#     print("#%d" %i, sum)