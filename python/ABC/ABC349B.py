S = input()

cnt = [0] * 26
for c in S:
    cnt[ord(c) - ord('a')] += 1
print(cnt)

cnt2 = [0] * (len(S) + 1)
for x in cnt:
    if x > 0:
        cnt2[x] += 1
print(cnt2)

print("Yes" if all(v in (0, 2) for v in cnt2) else "No")
