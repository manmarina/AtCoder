import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

N, T = map(int, input().split())
A = list(map(int, input().split()))  # 曲の長さ

start = [0]  # 各曲の再生開始時間
for i in range(N - 1):
    start.append(start[i] + A[i])
logging.debug(f"{start = }")

rest = T % sum(A)  # 最後の周回の残り時間
logging.debug(f"{rest = }")

for i in reversed(range(N)):  # 最後の曲から探索
    if rest > start[i]:  # 残り時間が、曲の開始時間よりもそいとき
        print(i + 1, rest - start[i])  # その差がその曲の再生時間
        break

"""
基本実装問題
プレイリストで再生される曲番号と、その曲の再生秒数を出力する。

https://atcoder.jp/contests/abc281/tasks/abc281_c
"""
