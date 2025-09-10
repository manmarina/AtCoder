S = input().strip()
n = len(S)
ans = 0

for mask in range(1 << (n - 1)):  # ビットマスクを生成 2**(n-1)
    cur = 0
    for i, ch in enumerate(S):
        cur = cur * 10 + int(ch)  # 数字を伸ばす
        if i == n - 1 or (mask >> i) & 1:  # 文字列の最後の文字か、ビットマスクが1の場所なら
            ans += cur
            cur = 0

print(ans)
