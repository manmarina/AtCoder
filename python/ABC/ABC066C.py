from collections import deque


n = int(input())
a = list(map(int, input().split()))

# リストへの追加
deq = deque()  # 先頭への追加を高速に行いたいので
for i in range(n):
    if i % 2 == 0:  # インデックスが偶数の時
        deq.append(a[i])  # 末尾に追加
    else:
        deq.appendleft(a[i])  # 先頭に追加

# 出力
if n % 2 == 0:  # nが偶数の時
    print(*deq)  # そのまま出力
else:  # nが奇数の時
    rev = reversed(deq)
    print(*rev)  # 逆順で出力

"""
計算量を削減したシミュレーション + 数学的な気づき系
偶奇を考える。
ソートはせずに、偶奇によりリストへの追加方向を変える。(deque()を活用)
出力時も、偶奇を考えて向きを変える。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2025/01/01/174846

https://atcoder.jp/contests/abc066/tasks/arc077_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6913e165-8278-8323-9698-776c7210262a
"""
