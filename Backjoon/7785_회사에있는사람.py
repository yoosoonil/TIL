import sys

N = int(input())
logs = dict()
for i in range(N):
    key, value = input().split()
    logs[key] = value
    logs["Baha"] = "enter"
    logs["Askar"] = "enter"
    logs["Baha"] = "leave"
    logs["Artem"] = "enter"

list_ = []
for key in logs:
    print(key)
    
    if logs[key] == "enter":
        list_.append(key)
