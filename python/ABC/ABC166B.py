N, K = map(int, input().split())

A = set()
for _ in range(K):
    d = int(input())
    A.update(map(int, input().split()))

# print(A)

print(N - len(A))
