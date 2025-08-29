N = int(input())

ab = [tuple(map(int, input().split())) for _ in range(N - 1)]

# print(ab)

deg = [0] * (N + 1)
for a, b in ab:
    deg[a] += 1
    deg[b] += 1

# print(deg)

# for d in deg:
#     if d == N - 1:
#         print("Yes")
#         break
# else:
#     print("No")
print("Yes" if any(d == N - 1 for d in deg) else "No")
