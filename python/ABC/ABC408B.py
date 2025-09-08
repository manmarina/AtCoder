N = int(input())
A = list(map(int, input().split()))

A = sorted(list(set(A)))
print(len(A))
print(*A)
