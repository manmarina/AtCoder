N = int(input())
P = list(map(int, input().split()))  # 長さ N-1。P[0] が P2 に対応

# 1-indexed の親配列を作る
par = [0] * (N + 1)
for i in range(2, N + 1):
    par[i] = P[i - 2]

# print(P)
# print(par)

ans = 0
cur = N
while cur > 1:
    cur = par[cur]
    ans += 1

    # print(cur)

print(ans)
