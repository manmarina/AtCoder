N, K = map(int, input().split())
S = input()

count = 0
for i, s in enumerate(S, 1):
    if s == 'o':
        count += 1
    if count == K:
        break

ans = S[:i] + 'x' * (N - i)
print(ans)
