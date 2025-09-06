N, R = map(int, input().split())
DA = [list(map(int, input().split()))for _ in range(N)]
# print(DA)

for d, a in DA:
    if d == 1:
        if 1600 <= R <= 2799:
            R += a
    else:  # d == 2
        if 1200 <= R <= 2399:
            R += a
print(R)
