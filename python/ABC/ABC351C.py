N = int(input())
A = list(map(int, input().split()))

line = []
for i in range(N):  # すべてのボールについて
    line.append(A[i])  # 列にボールを追加
    # 列のボールが2つ以上で、最後の2つのボールが同じ大きさの時
    while len(line) >= 2 and line[-1] == line[-2]:
        line.pop()  # ボールを取り出して
        line[-1] += 1  # 合体したボールを入れる
    # print(line)

print(len(line))  # 列のボールの数を出力

"""
シミュレーション系

けんちょんの解説
https://drken1215.hatenablog.com/entry/2024/09/25/003542
大きさが 2mのボールを 2 つ合わせると、2m+1のボールになることに注意しよう。

http://atcoder.jp/contests/abc351/tasks/abc351_c
"""
