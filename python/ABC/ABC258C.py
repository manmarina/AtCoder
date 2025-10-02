import sys


input = sys.stdin.readline
N, Q = map(int, input().split())
S = input().strip()
head = 0  # いまの先頭が元Sのどこか（0-index）

out = []
for _ in range(Q):
    t, x = input().split()
    x = int(x)
    if t == '1':
        x %= N
        head = (head - x) % N    # 右回転 x 回
        # print(head)
    else:  # t == '2'
        idx = (head + x - 1) % N
        out.append(S[idx])
print('\n'.join(out))

"""
シミュレーション（クエリ処理）
チャッピー
配列（文字列）を実際に回さず、先頭がどこかを指す変数 head だけを更新します。

https://atcoder.jp/contests/abc258/tasks/abc258_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68de24c5-cf84-8326-9723-69367118703f
"""
