S = input()
ok = set("ATGC")

cur = 0
ans = 0
for ch in S:
    if ch in ok:
        cur += 1
        if cur > ans:
            ans = cur
    else:
        cur = 0
print(ans)
