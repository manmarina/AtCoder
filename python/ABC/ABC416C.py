from itertools import product


N, K, X = map(int, input().split())
S = [input() for _ in range(N)]

ans = []
for combi in product(S, repeat=K):  # N^Kパターンの組み合わせ
    conc = ''.join(combi)  # 文字列を結合
    ans.append(conc)  # 結合した文字列をリストに追加
ans.sort()  # リストを昇順ソート
print(ans[X - 1])  # 辞書順でX番目を表示

"""
全探索
組み合わせ生成にdfsを使っても解けるらしい。

https://atcoder.jp/contests/abc416/tasks/abc416_c
"""
