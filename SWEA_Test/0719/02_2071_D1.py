import sys
sys.stdin = open("2071.txt", "r")

# number_list = [int(x) for x in input().split()]

# total = 0
# count = 0

# for n in number_list:
#     total += n
#     count += 1

# print(total / count)

T = int(input())

for tc in range(T):                      # T가 3이기에 3번 돌린다는 것 같음.
    numbers = input()
    numbers = numbers.split()
    numbers = list(map(int, numbers))
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
        average = round(total/count) 
    print(f'#{tc+1} {average}')