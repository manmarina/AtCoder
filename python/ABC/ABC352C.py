N = int(input())

A = []  # 肩の高さ
C = []  # 頭の大きさ
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    C.append(b - a)

print(sum(A) + max(C))  # 型の高さの累積 + 最も大きい頭の大きさ

"""
数学的な気づき系
数列の問題。
頭の大きい巨人を一番上にする。
チャッピーの式変形も参照して下さい。

https://atcoder.jp/contests/abc352/tasks/abc352_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690e1f27-9cf4-8323-b433-99fc9eb130fe
"""
