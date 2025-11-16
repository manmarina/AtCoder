H, W, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
# print(AB)

# 座標圧縮
# 逆変換（圧縮後の値 → 圧縮前の値）
A = [a for a, _ in AB]
B = [b for _, b in AB]
rows = sorted(set(A))
cols = sorted(set(B))

# 順変換（圧縮前の値 → 圧縮後の値)
row_id = {v: i + 1 for i, v in enumerate(rows)}  # 1-indexed
col_id = {v: i + 1 for i, v in enumerate(cols)}  # 1-indexed

# 出力
for a, b in AB:
    print(row_id[a], col_id[b])

"""
座標圧縮
座標圧縮の教育的な問題。
座標圧縮テンプレートを使用。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2021/08/11/023013

https://atcoder.jp/contests/abc213/tasks/abc213_c
"""
