sx, sy, tx, ty = map(int, input().split())
dx, dy = tx - sx, ty - sy

ans = []
# 1往復（まっすぐ）
ans.append("R" * dx + "U" * dy + "L" * dx + "D" * dy)
# 外周ループ（1マスふくらませる）
ans.append("D" + "R" * (dx + 1) + "U" * (dy + 1) + "L")
ans.append("U" + "L" * (dx + 1) + "D" * (dy + 1) + "R")

print("".join(ans))
