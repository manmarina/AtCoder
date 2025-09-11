N = int(input())

# 各人 i の証言を [(x1, y1), (x2, y2), ...] にまとめる。
A = []
for _ in range(N):
    m = int(input())
    st = []
    for _ in range(m):
        x, y = map(int, input().split())
        st.append((x - 1, y))  # 0-index
    A.append(st)
# print(A)

# 「正直者だと仮定した人」の証言だけを信じて矛盾がないかを確かめる。
ans = []
for mask in range(1 << N):  # 正直者候補集合
    ok = True
    for i in range(N):
        if (mask >> i) & 1:  # i を正直者と仮定
            for x, y in A[i]:
                if y == 1 and ((mask >> x) & 1) == 0:
                    ok = False
                    break
                if y == 0 and ((mask >> x) & 1) == 1:
                    ok = False
                    break
        if not ok:  # 二重ブレイクのために必要
            break
    if ok:  # 二重ブレイクしたあとに実行させないために必要
        ans.append(bin(mask).count("1"))

# print(ans)
print(max(ans))


"""
アルゴリズムの要点

入力の整理
各人 i の証言を [(x1, y1), (x2, y2), ...] にまとめる。
    x は人の番号（1-index → 0-indexに直すと楽）
    y は「正直者なら1、嘘つきなら0」

部分集合（= 正直者候補セット）をbitで表現
    mask の i ビット目が1なら「iは正直者」と仮定。

整合性チェック
 「正直者だと仮定した人」の証言だけを信じて矛盾がないかを確かめる。
    もし i が正直者（mask>>i & 1 == 1）なら、その証言 (x,y) について
        y==1 なら x も mask に含まれている必要あり
        y==0 なら x は mask から外れている必要あり
    1つでも破れたらその mask は無効

最大人数
    整合する mask の中で popcount(mask) が最大のものが答え。

計算量はだいたい O(2^N x 総証言数)。N=15 なら余裕です。

嘘つきの証言は一切参照しない（「正直者だと仮定した人」の証言だけでチェック）。
"""
