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
            total ^= cur_or  # XORは計算の順序によらないので随時おこなっても大丈夫
            cur_or = 0

    # 最後に残った部分とtotalとXORしてansに格納
    total ^= cur_or
    ans.append(total)

# print(ans)
print(min(ans))

"""
ビット全探索
bit全探索

何を最小化する問題？
    長さ N の配列 A を、いくつかの連続区間に分割する。
    各区間の要素を ビットOR した値を1つずつ作る。
    それらをすべて ビットXOR した値をつくる。
    この最終値を最小化する分割を探す。

核心となる観察
    区間の切れ目は「要素間（N-1 箇所）」にしか現れない。
    よって「切る／切らない」を各位置で選ぶと、分割は 2^(N-1) 通りに一致。
    ある分割が決まれば、左から順に
    「現在の区間OR」を更新し、切れ目に来たらそのORを答えXORへ畳み込む、を繰り返せばよい。
    *ビット単位OR、ビット単位XORとも計算の順序によらないことが証明できます

解法（ビット全探索：切れ目マスク）
    マスク mask の i ビット（0-indexで i=0..N-2）が 1 なら、A[i] と A[i+1] の間で切る。
    左から走査し、区間ORを進め、切る所で答えXORに反映。最後の区間も忘れず反映。
"""
