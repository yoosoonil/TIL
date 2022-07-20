import sys

sys.stdin = open('0720/02_2050.txt', "r")

container = input('')
for i in container:
     ans = ord(i) - 64
     print(ans, end = ' ')