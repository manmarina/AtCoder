from collections import Counter

A = list(map(int, input().split()))
cnt = Counter(A)
has3 = [v for v, c in cnt.items() if c >= 3]  # 3枚以上のカードのリスト
print(cnt)
print(has3)

ok = False
for v in has3:
    if any((u != v and c >= 2)
           for u, c in cnt.items()):  # ある3枚以上のカード以外に2枚以上のカードがあるか探索
        ok = True
        break
print("Yes" if ok else "No")
