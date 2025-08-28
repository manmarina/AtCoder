N, X = map(int, input().split())
A = list(map(int, input().split()))

print(*list(a for a in A if a != X))
