from itertools import combinations
from collections import Counter

A = list(map(int, input().split()))

for cards in combinations(A, 5):
    # print(sorted(cards))
    cnt = Counter(cards)
    if sorted(cnt.values()) == [2, 3]:  # 2枚と3枚
        print("Yes")
        break
else:
    print("No")
