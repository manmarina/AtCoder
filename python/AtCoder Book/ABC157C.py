N, M = map(int, input().split())
sc = [tuple(map(int, input().split())) for _ in range(M)]

# 各桁の指定値を管理（未指定は None）
digits = [None] * N

# 矛盾チェック（同じ桁に違う値が来たらNG）
for s, c in sc:
    idx = s - 1
    if digits[idx] is None:
        digits[idx] = c
    elif digits[idx] != c:
        print(-1)
        exit()

# 先頭桁チェック（N>1 のときは 0 始まりはNG）
if N > 1 and digits[0] == 0:
    print(-1)
    exit()

# 最小値で埋める
if digits[0] is None:
    digits[0] = 0 if N == 1 else 1
for i in range(1, N):
    if digits[i] is None:
        digits[i] = 0

print(int("".join(map(str, digits))))
