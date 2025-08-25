A, B, K = map(int, input().split())

ans = set()
left_end = min(A + K - 1, B)
for i in range(A, left_end + 1):
    ans.add(i)

right_start = max(B - K + 1, A)
for i in range(right_start, B + 1):
    ans.add(i)

ans = sorted(list(ans))
print(*ans, sep='\n')
