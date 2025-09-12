N, X = map(int, input().split())
a = list(map(int, input().split()))
print(a)

result = 0

# X以上のキャンディは最初に食べておく
for i in range(N):
    if a[i] > X:
        result += a[i] - X
        a[i] = X
print(a)
print(result)

for i in range(N - 1):
    if a[i] + a[i + 1] > X:
        result += a[i] + a[i + 1] - X
        a[i + 1] = X - a[i]

print(a)
print(result)
