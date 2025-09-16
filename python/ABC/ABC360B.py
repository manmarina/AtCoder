S, T = input().split()

res = False
for w in range(1, len(S)):          # 1 <= w < |S|
    for c in range(w):              # 0 <= c < w
        U = ""
        for k in range(c, len(S), w):
            U += S[k]
        if U == T:
            res = True

print("Yes" if res else "No")
