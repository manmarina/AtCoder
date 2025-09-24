import sys

input = sys.stdin.readline
N, W = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]  # (a, b)
print(AB)

# おいしさ a が大きい順に
AB.sort(key=lambda x: x[0], reverse=True)

ans = 0
for a, b in AB:
    if W == 0:
        break
    take = min(W, b)
    ans += a * take
    W -= take

print(ans)

"""
貪欲法
チャッピー
価値密度が高いものから取ればよい。

https://atcoder.jp/contests/abc229/tasks/abc229_c
https://chatgpt.com/c/68d29f01-2348-8323-ba9f-b33fd24b0d56
"""
