N, K = map(int, input().split())
A = list(map(int, input().split()))

i = 1
for a in A:
    i *= a
    if i >= 10**K:
        i = 1
print(i)
