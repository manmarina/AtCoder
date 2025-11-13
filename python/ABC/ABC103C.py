N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans += a - 1

print(ans)

"""
法則を見つける系
けんちょん
https://drken1215.hatenablog.com/entry/2018/07/21/224100
各項がai - 1の時がfの最大値であり、そのような解があることに気づく。
その時のmは最小公倍数-1であることに気づく。

https://atcoder.jp/contests/abc103/tasks/abc103_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69159c01-62d8-8323-963e-d5cb6afa30d2
"""
