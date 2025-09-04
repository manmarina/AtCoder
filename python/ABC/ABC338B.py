from collections import Counter

S = input()

cnt = Counter(S)
print(min(cnt.keys(), key=lambda x: (-cnt[x], x)))
