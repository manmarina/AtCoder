N, M = map(int, input().split())
A = list(map(int, input().split()))

seen = [False] * (M + 1)
kinds = 0
r = None  # 1..M が初めて揃う位置(1-index)

for i, a in enumerate(A, start=1):  # 1-index
    if not seen[a]:
        seen[a] = True
        kinds += 1
        if kinds == M:
            r = i
            break

if r is None:
    print(0)
else:
    print(N - r + 1)
