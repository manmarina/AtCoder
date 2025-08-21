A, B, C = map(int, input().split())

m = max(A, B, C)
D = (m - A) + (m - B) + (m - C)

if D % 2 == 0:
    print(D // 2)
else:
    print(D // 2 + 2)
