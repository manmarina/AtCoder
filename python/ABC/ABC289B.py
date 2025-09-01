N, M = map(int, input().split())
A = list(map(int, input().split())) if M else []

S = set(A)  # レがある位置 i（= i と i+1 が繋がる）

ans = []
cur = 1
while cur <= N:
    r = cur
    while r <= N - 1 and r in S:
        r += 1
    # 区間 [cur, r] を逆順で追加
    for x in range(r, cur - 1, -1):
        ans.append(x)
    cur = r + 1

print(*ans)
