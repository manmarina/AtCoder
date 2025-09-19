import sys
from itertools import permutations

input = sys.stdin.readline
N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]


def dist1(a, b):  # カウント1ならTrue、そうでなければFalseを返す
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1


# 事前にカウントが1かどうかを表に
ok = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            ok[i][j] = dist1(S[i], S[j])
# print(ok)

# 順列全探索
for perm in permutations(range(N)):
    good = True
    for i in range(N - 1):
        # カウントが1でなければその順列はパスして次の順列へ
        if not ok[perm[i]][perm[i + 1]]:
            good = False
            break
    if good:
        print("Yes")
        break
else:
    print("No")

"""
順列全探索
自分のロジックと違うのは、事前にカウント1かどうかを表にしている点のみ

隣り合う2文字列のハミング距離（違う文字数）がちょうど1になるような並べ替え（順列）が存在するか？」の判定
同じ長さの文字列 s, t について、位置ごとに比較して異なる箇所数を数える。
本問では「距離=1」を満たすかだけ使うので、2以上になったら途中で打ち切る早期終了が有効。
"""
