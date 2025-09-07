T = int(input())
tc = [list(map(int, input().split())) for _ in range(T)]
# print(tc)

for na, nb, nc in tc:
    d = abs(na - nc)
    mn = min(na, nb, nc)
    ma = na - mn
    mc = nc - mn
    p = min(min(ma, mc), max(ma, mc) // 2)
    print(mn + p)
