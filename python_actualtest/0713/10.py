# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

# Input

# numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# Output

# 3

numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

a = 0
for n in numbers:
    if n == 5:
        a += 1
print(a)