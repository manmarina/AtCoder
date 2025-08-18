from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)  # 連想配列：値→出現回数
total = N * (N - 1) // 2
same = sum(c * (c - 1) // 2 for c in cnt.values())
print(total - same)
