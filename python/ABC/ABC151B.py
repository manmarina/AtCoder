N, K, M = map(int, input().split())
A = list(map(int, input().split()))

hope = N * M - sum(A)
if hope > K:
    print(-1)
else:
    print(max(0, hope))
