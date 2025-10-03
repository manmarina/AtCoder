def cross(ax, ay, bx, by):  # ベクトルの外積を計算
    return ax * by - ay * bx


def is_convex(A, B, C, D):
    # ベクトル差を作るためのヘルパ
    def vec(P, Q):  # P->Q
        return (Q[0] - P[0], Q[1] - P[1])

    AB = vec(A, B)
    BC = vec(B, C)
    CD = vec(C, D)
    DA = vec(D, A)

    z1 = cross(AB[0], AB[1], BC[0], BC[1])  # ∠ABC
    z2 = cross(BC[0], BC[1], CD[0], CD[1])  # ∠BCD
    z3 = cross(CD[0], CD[1], DA[0], DA[1])  # ∠CDA
    z4 = cross(DA[0], DA[1], AB[0], AB[1])  # ∠DAB

    # 共線含むなら凸ではない
    if z1 == 0 or z2 == 0 or z3 == 0 or z4 == 0:
        return False

    # 符号がそろっていれば凸
    pos = (z1 > 0) + (z2 > 0) + (z3 > 0) + (z4 > 0)
    neg = (z1 < 0) + (z2 < 0) + (z3 < 0) + (z4 < 0)
    return pos == 4 or neg == 4


pts = [tuple(map(int, input().split())) for _ in range(4)]

A, B, C, D = pts
print("Yes" if is_convex(A, B, C, D) else "No")


"""
数学的な気付き系
チャッピー
外積(クロス積)と向き判定(ccw)

4点 A,B,C,D をこの順に結んだ四角形が「凸かどうか」を判定するだけです。

https://atcoder.jp/contests/abc266/tasks/abc266_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68df436d-962c-8323-8165-b20aef8e22ee
"""
