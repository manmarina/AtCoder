perm = []
count = 0
for i in range(8):
    for j in range(8):
        for k in range(8):
            for l in range(8):
                for m in range(8):
                    for n in range(8):
                        for o in range(8):
                            for p in range(8):
                                count += 1
                                temp = [i, j, k, l, m, n, o, p]
                                if len(temp) == len(set(temp)):
                                    perm.append(temp)

print(count)
print(len(perm))
# ABC098 C - Attention
N = int(input().strip())
S = input().strip()

# 累積和（長さ N+1, 先頭0）
prefW = [0] * (N + 1)
prefE = [0] * (N + 1)

for i, ch in enumerate(S, 1):
    prefW[i] = prefW[i - 1] + (ch == 'W')
    prefE[i] = prefE[i - 1] + (ch == 'E')
print(prefW)
print(prefE)

totalE = prefE[N]

ans = 10**9
for i in range(N):
    left_W = prefW[i]              # 左側のW（左はE向きが正解なのでWは反転必要）
    right_E = totalE - prefE[i + 1]  # 右側のE（右はW向きが正解なのでEは反転必要）
    ans = min(ans, left_W + right_E)

print(ans)
