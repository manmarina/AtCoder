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

"""
ビット全探索
区切り位置の bit全探索（基本解）

桁間は n-1 箇所。そこに + を入れるか入れないかの 2^(n-1) 通りを全探索。
マスク mask の i-bit（0 ≤ i < n-1）が 1 なら「i と i+1 の間に + を入れる」。
実装は「現在の値 cur を 10 倍して次の桁を足す」を繰り返し、区切りが来たら sum に加えて cur を 0 に戻す。最後の塊も忘れずに加える。
文字列スライスして int(s[l:r]) を毎回作るより、この“伸ばして足す”やり方が高速＆簡潔。
"""
