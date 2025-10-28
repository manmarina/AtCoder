import sys
input = sys.stdin.readline

# 　入力
N, M = map(int, input().split())
A = []
for _ in range(M):
    data = list(map(int, input().split()))
    k = data[0]
    vals = data[1:]
    A.append(vals)
B = list(map(int, input().split()))

# B の値が「何番目に出てくるか」を辞書にしておく
pos = {value: i + 1 for i, value in enumerate(B)}  # value -> 1-based index

cnt = [0] * (N + 1)  # cnt[i] = cnt[食べられるようになる日] = 食べられるようになった料理の数

# 各料理ごとにすべての食材を見て一番遅い日付を求める
for vals in A:
    mx = 0
    for v in vals:
        # 食材の名前を克服する日付に変更する
        p = pos[v]  # ← 辞書なので速い O(1)
        if p > mx:  # 一番遅い日付に更新
            mx = p
    cnt[mx] += 1  # 一番遅い日付のカウントを増やす

# print(A)
# print(pos)
# print(cnt)

# 累積和を出力
ans = 0
for i in range(1, N + 1):
    ans += cnt[i]
    print(ans)


"""
計算量を削減したシミュレーション
チャッピーにより高速化してAC
六月
https://x.com/june19312/status/1914148087905587212"
食材の名前を克服する日付に変更する。
使われている食材で、最大の日付が克服する日。

B.index(x) はリスト線形探索なので O(N) -> posという変換用辞書を用意して O(1)に改善

https://atcoder.jp/contests/abc402/tasks/abc402_c
https://chatgpt.com/c/6900653a-a868-8320-b956-3c081ae46123
"""
