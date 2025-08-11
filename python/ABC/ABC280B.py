N = int(input())
S = list(map(int, input().split()))

print(S[0], end='')
for i in range(1, N):
    print('', S[i] - S[i - 1], end='')
print()
