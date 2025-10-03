import sys

input = sys.stdin.readline
n = int(input())
cnt = {}  # s -> 出現回数
out = []
for _ in range(n):
    s = input().rstrip("\n")
    k = cnt.get(s, 0)
    if k == 0:
        out.append(s)
    else:
        out.append(f"{s}({k})")
    cnt[s] = k + 1
print("\n".join(out))


"""
文字列処理 x 連想配列（ハッシュマップ）
チャッピー

https://atcoder.jp/contests/abc261/tasks/abc261_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68de2fb5-575c-8321-89a9-d45ab3b032c
"""
