import math

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# print(A)
# print(B)

idx_A, min_A = min(enumerate(A), key=lambda x: x[1])
idx_B, min_B = min(enumerate(B), key=lambda x: x[1])

# print(idx_A, min_A)
# print(idx_B, min_B)

if idx_A == idx_B:
    min_A2 = min((a for i, a in enumerate(A) if i != idx_A), default=math.inf)
    min_B2 = min((a for i, a in enumerate(B) if i != idx_B), default=math.inf)

    # print(min_A2)
    # print(min_B2)

    print(min(min_A2, min_B2, min_A + min_B))
else:
    print(max(min_A, min_B))
