N = int(input())
A = list(map(int, input().split()))

# 切れ目をいれる箇所はN-1 ビットマスク作成
ans = []
for mask in range(1 << (N - 1)):
    cur_or = 0
    total = 0
    # print(bin(mask))

    # 数列Aを順に処理
    for i in range(N):
        cur_or |= A[i]

        # ビットマスクが1のところでカットしてtotalとXORする
        if (mask >> i) & 1:
            total ^= cur_or
            cur_or = 0

    # 最後に残った部分とtotalとXORしてansに格納
    total ^= cur_or
    ans.append(total)

# print(ans)
print(min(ans))
