S = set(input())

length = len(set(S))
count = 1
if length == 3:
    count = 6
elif length == 2:
    count = 3

print(count)
