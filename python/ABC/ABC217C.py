N = int(input())
P = [0] + list(map(int, input().split()))  # 1-index

Q = [0] * (N + 1)  # 1-index
for i in range(1, N + 1):
    Q[P[i]] = i

print(*Q[1:])

"""
基本実装問題
自力解

与えられた順列 P の逆順列 Q を作るだけの基本実装問題です。
配列の逆写像（順列の逆関数）：一度の走査で作れます。
インデックスの扱い（1-indexed vs 0-indexed）：AtCoderは1始まりの出力が多いので注意。

時間計算量 O(N)、メモリ O(N)。
"""
