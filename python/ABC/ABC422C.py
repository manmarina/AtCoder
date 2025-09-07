T = int(input())
tc = [list(map(int, input().split())) for _ in range(T)]
# print(tc)

for na, nb, nc in tc:
    total = na + nb + nc
    print(min(na, nc, total // 3))
