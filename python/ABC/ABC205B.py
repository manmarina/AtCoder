N = int(input())
A = set(map(int, input().split()))

ok = {i for i in range(1, N + 1)}
print("Yes" if ok == A else "No")
