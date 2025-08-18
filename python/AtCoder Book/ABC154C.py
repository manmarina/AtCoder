from collections import Counter

N = int(input())
A = list(map(int, input().split()))

for count in Counter(A).values():
    if count > 1:
        print("NO")
        exit()
print("YES")
