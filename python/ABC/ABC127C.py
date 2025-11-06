from collections import Counter


N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]

# 変化配列を作成
change = [0] * (N + 2)
for l, r in LR:
    change[l] += 1
    change[r + 1] -= 1
# print(change)

# いもす配列を作成
imos = [0]
for i in range(1, N + 1):
    imos.append(imos[i - 1] + change[i])
# print(imos)

cnt = Counter(imos)  # 通過可能点の数をカウント
# print(cnt)
print(cnt[M])  # 通過可能点の数がM個あるところの数を表示

"""
いもす法（imos法）
すべてのゲートで共通する通過可能点を探す。

けんちょんの解説
261Aと同じように区間の交差で簡単に求めることもできる。
https://drken1215.hatenablog.com/entry/2019/06/11/103300

https://atcoder.jp/contests/abc127/tasks/abc127_c
"""
