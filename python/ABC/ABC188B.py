N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

prod = sum(a * b for a, b in zip(A, B))
print("Yes" if prod == 0 else "No")
