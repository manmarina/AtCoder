import sys
import heapq

it = iter(sys.stdin.read().split())
Q = int(next(it))
h = []
out = []
for _ in range(Q):
    t = int(next(it))
    if t == 1:
        x = int(next(it))
        heapq.heappush(h, x)
    else:
        out.append(str(heapq.heappop(h)))
print("\n".join(out))

"""
heapq は、Python 標準ライブラリに入っている「最小ヒープ（min-heap） を扱うモジュール」です。
リストを内部表現として使い、常に**最小要素が先頭（index 0）**に来るデータ構造を O(log n) で更新できます。

何ができる？
heapq.heappush(h, x)：x を挿入（O(log n)）
heapq.heappop(h)：最小要素を取り出し（O(log n)）
h[0]：最小要素を見るだけ（O(1)）
heapq.heapify(a)：普通のリスト a をヒープに変換（O(n)）

おまけ
heappushpop(h, x)：push してから pop（1回で済む最適化）
heapreplace(h, x)：pop してから push（ヒープが空でない前提）
nsmallest / nlargest：上位 k 個の抽出
"""
