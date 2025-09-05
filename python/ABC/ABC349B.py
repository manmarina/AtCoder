from collections import Counter

S = input()

cnt = Counter(S)
# print(cnt)

ans = []
for i in range(len(S) + 1):  # len(S) "+1"　が重要 例：S="aaaaa"
    ans.append(len([c for c in cnt.values() if c == i]))
# print(ans)

print("Yes" if all(a in (0, 2) for a in ans) else "No")
