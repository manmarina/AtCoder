N, M, T = map(int, input().split())
A = list(map(int, input().split()))
bonus = {}
for _ in range(M):
    x, y = map(int, input().split())
    bonus[x - 1] = y

print(bonus)

time = T
for i in range(N):
    if i in bonus:
        T += bonus[i]
    time -= A[i]
