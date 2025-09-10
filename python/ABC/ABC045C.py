S = input().strip()
n = len(S)

ans = []
for mask in range(1 << (n - 1)):  # ビットマスクを生成 2**(n-1)
    cur = 0
    temp = 0
    for i, ch in enumerate(S):
        cur = cur * 10 + int(ch)  # 数字を伸ばす
        if i == n - 1 or (mask >> i) & 1:  # 文字列の最後の文字か、ビットマスクが1の場所なら
            temp += cur
            cur = 0
    ans.append(temp)

# print(ans)
print(sum(ans))
