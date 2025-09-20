import sys

input = sys.stdin.readline
N, K = map(int, input().split())

# abを連想配列として格納
cnt = {}
for _ in range(N):
    a, b = map(int, input().split())
    cnt[a] = cnt.get(a, 0) + b  # 合算
# print(cnt)

cur = 0
for a in sorted(cnt):           # a 昇順
    cur += cnt[a]               # 累積
    if cur >= K:                # 初めて K に到達/超過
        print(a)
        break


"""
累積和（prefix和）
チャッピー
abを連想配列として格納する点が自力解と異なる

 狙いはシンプルです：
巨大配列を作る代わりに、
値で昇順ソート → 累積和が K に届いた瞬間の値を答える、これだけです。

この問題の注意点として、Sを具体的に作ろうとすると、最大で
10**10くらいのサイズになってメモリも計算時間も飛んでしまうので注意。。。
"""
