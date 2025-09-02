N, M = map(int, input().split())
seen = set()  # 隣接で現れた無向ペアを格納

for _ in range(M):
    A = list(map(int, input().split()))
    for i in range(N - 1):
        x, y = A[i], A[i + 1]
        if x > y:
            x, y = y, x
        seen.add((x, y))  # setにsetは格納できないので、ソートしたtupleを追加

print(seen)

total_pairs = N * (N - 1) // 2
ans = total_pairs - len(seen)
print(ans)
