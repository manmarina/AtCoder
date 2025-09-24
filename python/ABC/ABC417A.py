N, A, B = map(int, input().split())
S = [*input()]
# print(S)

print(*S[A:N - B], sep='')
