N, Q = map(int, input().split())
TAB = [list(map(int, input().split())) for _ in range(Q)]

G = [set() for _ in range(N + 1)]
# print(G)

for t, a, b in TAB:
    if t == 1:
        G[a].add(b)
    elif t == 2:
        G[a].discard(b)  # 存在しなくてもOK
    else:  # t == 3:
        if b in G[a] and a in G[b]:
            print("Yes")
        else:
            print("No")
# print(G)

"""
RE & TLE

チャッピーによる解説
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690218b0-766c-8322-b574-4399935762e2
セットはメモリ使用量が多いので、setをN個確保するとメモリ使用量が莫大になる。
メモリが膨らんで MemoryError→RE になる可能性がある。
計算量はすべてO(1)だが、メモリ使用量が逼迫してTLEも併発しているかもしれない。
-> setはひとつにして、タプルでデータを追加すればメモリ使用量を削減できる。

https://atcoder.jp/contests/abc278/tasks/abc278_c
"""
