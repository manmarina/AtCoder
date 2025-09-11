import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

INF = 1 << 60
ans = INF

# 切れ目は N-1 箇所
for mask in range(1 << (N - 1)):
    cur_or = 0   # 現在区間のOR
    total = 0    # 区間ORをXORで畳み込んだ値
    for i in range(N):
        cur_or |= A[i]
        # i の位置で切るか？（i は区間の末尾候補）
        if i < N - 1 and (mask >> i) & 1:
            total ^= cur_or
            cur_or = 0
    total ^= cur_or  # 最後の区間
    ans = min(ans, total)

print(ans)
