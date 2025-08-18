from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for a in A:
    cnt[a] += 1

total = N * (N - 1) // 2
same = 0
for c in cnt.values():
    same += c * (c - 1) // 2

print(total - same)
