N = int(input())
ABCD = [list(map(int, input().split())) for _ in range(N)]
# print(ABCD)

covered = [[False] * 100 for _ in range(100)]
# print(covered)

for A, B, C, D in ABCD:
    for i in range(C, D):
        for j in range(A, B):
            covered[i][j] = True
print(sum(1 for row in covered for i in row if i))
# print(sum(row.count(True) for row in covered))
