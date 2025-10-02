import sys

input = sys.stdin.readline
N = int(input())
S = [input().strip() for _ in range(N)]

ans = 10**9
for d in range(10):
    cnt = [0]*10  # 位置ごとの衝突数
    ch = str(d)
    for s in S:
        p = s.index(ch)  # s は長さ10なので O(10) で十分
        cnt[p] += 1
    # この桁 d をそろえるのに必要な時間＝各位置の「最後に止まる時刻」の最大
    mx = 0
    for p in range(10):
        if cnt[p] > 0:
            mx = max(mx, p + 10*(cnt[p]-1))  # 時間が衝突したら10秒加算
    ans = min(ans, mx)

print(ans)

"""
シミュレーション
チャッピー

分類：周期シミュレーション／カウント（バケット）＋貪欲（最悪時刻の最小化）
着眼点：各桁は 10 秒周期で同じ位置に戻る（位置は 0〜9）。同じ桁を同じ「位置」で狙うと衝突して、10 秒待ちが積み増しされる。

https://atcoder.jp/contests/abc252/tasks/abc252_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68ddf5d1-390c-8326-b430-433a93f34cd1
"""
