N = int(input())

for i in range(1, N + 1):
    print(str("*" * i).rjust(N))    # rjust는 오른쪽정렬. ljust는 왼쪽정렬.