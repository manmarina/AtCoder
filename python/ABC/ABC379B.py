N, K = map(int, input().split())
S = input()

run = 0
ans = 0
for s in S:
    if s == 'O':
        run += 1
    else:
        ans += run // K
        run = 0
ans += run // K
print(ans)
