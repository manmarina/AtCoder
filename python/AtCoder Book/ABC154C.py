from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

dd = defaultdict(int)
for a in A:
    if dd[a] >= 1:
        print("NO")
        exit()
    else:
        dd[a] += 1
print("YES")
