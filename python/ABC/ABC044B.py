from collections import Counter

w = input()
cnt = Counter(w)
print("Yes" if all(v % 2 == 0 for v in cnt.values()) else "No")
