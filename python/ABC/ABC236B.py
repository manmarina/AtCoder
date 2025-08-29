from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
print(*[k for k, v in cnt.items() if v == 3])
