N, A, B = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    num = sum(map(int, str(i)))
    if A <= num <= B:
        ans += i
print(ans)
