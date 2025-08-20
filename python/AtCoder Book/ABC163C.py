from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

dd = defaultdict(int)
for a in A:
    a -= 1
    dd[a] += 1

# print(dd)

for i in range(N):
    if i in dd:
        print(dd[i])
    else:
        print(0)
