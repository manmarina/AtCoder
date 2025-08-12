N, M, T = map(int, input().split())
A = [0] + list(map(int, input().split()))

bonus = [0] * (N + 1)
for i in range(M):
    X, Y = map(int, input().split())
    bonus[X] = Y

# print(A)
# print(bonus)

for i in range(1, N):
    T += bonus[i]
    T -= A[i]

    if T <= 0:
        print("No")
        # print(T)
        break
else:
    print("Yes")
    # print(T)
