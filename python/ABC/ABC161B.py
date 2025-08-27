N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for a in A:
    # if a < sum(A) / (4 * M):
    if a * (4 * M) < sum(A):
        count += 1
print("Yes" if N - count >= M else "No")
