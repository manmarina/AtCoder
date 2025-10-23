# 入力
input()                          # A の個数（使わない）
A = list(map(int, input().split()))
input()                          # B の個数（使わない）
B = list(map(int, input().split()))
input()                          # C の個数（使わない）
C = list(map(int, input().split()))

# すべての a+b+c の組み合わせをセットに格納
S = set()
for a in A:
    for b in B:
        for c in C:
            S.add(a + b + c)

# クエリ
input()                          # X の個数（使わない）
X = list(map(int, input().split()))

# 各クエリに対して存在判定
for x in X:
    if x in S:
        print("Yes")
    else:
        print("No")


"""
工夫して探索の通り数を減らす「全探索 + 枝刈り」

A,B,C からそれぞれ1 個ずつ要素を選ぶ方法は N x M x L 通り
予めこれらを全て計算して set などで保持しておく

https://atcoder.jp/contests/abc344/tasks/abc344_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68f9f962-ac64-8321-b753-06259fc39c71
"""
