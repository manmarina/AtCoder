N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 番兵を追加（a-1, a+1 の境界対策） 1-indexed
# 番兵は白と同様の働きをする
v = [False] * (N + 2)
ans = 0  # 黒の連続区間の数

for a in A:
    if not v[a]:  # 白いとき
        v[a] = True
        if not v[a - 1] and not v[a + 1]:  # 左右が白ければ
            ans += 1
        elif v[a - 1] and v[a + 1]:  # 左右が黒ければ
            ans -= 1
    else:  # 黒いとき
        v[a] = False
        if v[a - 1] and v[a + 1]:  # 左右が黒ければ
            ans += 1
        elif not v[a - 1] and not v[a + 1]:  # 左右が白ければ
            ans -= 1
    print(ans)

"""
計算量を削減したクエリ処理

Yuulis
https://yuulis.hatenablog.com/entry/ABC-411-C
考察に書かれている左右マス状況8通りのうち、値が変化する4通りを実装している

https://atcoder.jp/contests/abc411/tasks/abc411_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68fb8b19-0048-8324-bf95-66b322b2bd20
"""
