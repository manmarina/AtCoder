N, K = map(int, input().split())
A = list(map(int, input().split()))

one = A.index(1)  # 1の位置を探す
# print(one)

ans = 10**6
for i in range(K):  # 1を含むK通りの範囲を探索
    right = one + i  # 選択した範囲の右端のインデックス
    rt = 0
    if right < N - 1:  # 右端に隙間がある時
        rt = -(-(N - 1 - right) // (K - 1))  # 右側を選択する回数　切り上げ除算

    left = one + i - K + 1  # 選択肢した範囲の左端のインデックス
    lt = 0
    if left > 0:  # 左端に隙間がある時
        lt = -(-left // (K - 1))  # 左側を選択する回数　切り上げ除算

    # print("right:", right, "left:", left, "rt:", rt, "lt:", lt)
    ans = min(ans, lt + rt + 1)  # 左右を選択した回数と、最初の選択1回を合計した数が最小なら更新

print(ans)


"""
計算量を削減したシミュレーション
要素は1を含むので、すべての要素を1にするのがゴール。
ということは、最初に選択するのは1を含む範囲。
この範囲の選択の仕方がK通りあるので、K通りを全探索する。
選択した範囲の左右のエリアを選択する回数をO(1)で求める。

WAのケース
4 4
1 2 3 4
を修正してAC!

けんちょんの解説
https://drken1215.hatenablog.com/entry/2018/06/24/003500

https://atcoder.jp/contests/abc101/tasks/arc099_a
"""
