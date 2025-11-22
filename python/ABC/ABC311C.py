N = int(input())
A = [0] + list(map(int, input().split()))  # 1-indexed
print(A)

# Step1: とにかく歩いてサイクル入口を探す
visited = [False] * (N + 1)
v = 1
while not visited[v]:
    visited[v] = True
    v = A[v]

start = v  # サイクル内のどこか

# Step2: サイクルの長さを測る
v = A[start]
cycle = [start]
while v != start:
    cycle.append(v)
    v = A[v]

# Step3: 出力
print(len(cycle))
print(*cycle)

"""
DFS不使用
functional graphのサイクル検出の問題。

Functional グラフとは、
各頂点 iに対して、その頂点を始点とする有向辺が 1 本だけ出ているような有向グラフです。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2023/07/24/030543
https://drken1215.hatenablog.com/entry/2023/05/20/200517

https://atcoder.jp/contests/abc311/tasks/abc311_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69212e6e-d978-8321-a3b8-304a11f76e83
"""
