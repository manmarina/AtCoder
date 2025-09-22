N = int(input())
P = list(map(int, input().split()))

ans = [0] * (N + 1)          # 1-indexed で扱う
for i, p in enumerate(P, start=1):
    ans[p] = i               # Q_{p} = i

print(*ans[1:])              # 1..N を出力

"""
基本実装問題
チャッピー
自力解と同じロジック

与えられた順列 P の逆順列 Q を作るだけの基本実装問題です。
配列の逆写像（順列の逆関数）：一度の走査で作れます。
インデックスの扱い（1-indexed vs 0-indexed）：AtCoderは1始まりの出力が多いので注意。

時間計算量 O(N)、メモリ O(N)。
"""
