N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))

seen = [False] * (N + 1)
a = X
count = 0
while not seen[a]:
    seen[a] = True
    a = A[a]
    count += 1
print(count)
