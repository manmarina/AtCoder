N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mx = max(A)
top = {i + 1 for i, a in enumerate(A) if a == mx}
bad = set(B)

# print(top)
# print(bad)

print("Yes" if top & bad else "No")
