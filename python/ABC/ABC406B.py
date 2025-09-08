N, K = map(int, input().split())
A = list(map(int, input().split()))

T = 10 ** K
x = 1
for a in A:
    p = x * a
    if p >= T:
        x = 1
    else:
        x = p
print(x)
