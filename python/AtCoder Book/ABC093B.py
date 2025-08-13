A, B, K = map(int, input().split())

answer = set()
left_end = min(A + K - 1, B)
for i in range(A, left_end + 1):
    answer.add(i)

right_start = max(A, B - K + 1)
for i in range(right_start, B + 1):
    answer.add(i)

print(*sorted(answer))
