N, K = map(int, input().split())
A = list(map(int, input().split()))

go = 0
rem = K
for a in A:
    if a <= rem:
        rem -= a
    else:
        go += 1
        rem = K - a
go += 1
print(go)
