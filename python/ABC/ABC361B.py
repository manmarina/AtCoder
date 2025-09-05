a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

# 1次元区間[A,B]と[C,D]の正の長さの交差条件は、min(B,D)-max(A,C)>0


def positive_overlap(lo1, hi1, lo2, hi2) -> bool:
    return min(hi1, hi2) - max(lo1, lo2) > 0


x1, X1 = min(a, d), max(a, d)
y1, Y1 = min(b, e), max(b, e)
z1, Z1 = min(c, f), max(c, f)

x2, X2 = min(g, j), max(g, j)
y2, Y2 = min(h, k), max(h, k)
z2, Z2 = min(i, l), max(i, l)

ok = (positive_overlap(x1, X1, x2, X2) and
      positive_overlap(y1, Y1, y2, Y2) and
      positive_overlap(z1, Z1, z2, Z2))

print("Yes" if ok else "No")
