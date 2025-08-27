N, K = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
ans = sum(v for i, v in enumerate(p) if i < K)
print(ans)
