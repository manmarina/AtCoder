import sys

input = sys.stdin.readline
N = int(input())
M = 2 * N + 1

used = [False] * (M + 1)
p = 1  # 次に出す候補（最小の未使用を指すポインタ）

while True:
    # 自分の手：最小の未使用を出す
    while p <= M and used[p]:
        p += 1
    if p <= M:
        print(p, flush=True)
        used[p] = True
    else:
        # もう出す数がない（通常はここに来ないが安全策）
        print(0, flush=True)
        exit()

    # 相手の手を読む
    a = int(input())
    if a == 0:
        exit()  # 終了
    used[a] = True

"""
インタラクティブ問題
チャッピー

https://atcoder.jp/contests/abc244/tasks/abc244_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68dd16d1-9b0c-8326-a494-2a58af7ae666
"""
