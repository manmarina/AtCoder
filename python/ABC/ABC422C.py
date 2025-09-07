T = int(input())
tc = [list(map(int, input().split())) for _ in range(T)]
# print(tc)

for na, nb, nc in tc:
    if min(na, nb, nc) != nb:
        print(min(na, nc))
    else:
        ans = nb
        na -= nb
        nc -= nb
        ans += min(min(na, nc), max(na, nc) // 2)
        print(ans)
