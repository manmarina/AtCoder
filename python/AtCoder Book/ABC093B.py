A, B, K = map(int, input().split())

answer = set()
for i in range(A, A + K):
    if i <= B:
        answer.add(i)

for i in range(B, B - K, -1):
    if A <= i:
        answer.add(i)

print(*sorted(answer))
