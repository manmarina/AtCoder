N, M, T = map(int, input().split())
A = [0] + list(map(int, input().split()))
bonus = {}
for _ in range(M):
    x, y = map(int, input().split())
    bonus[x] = y

# print(A)
# print(bonus)


for i in range(1, N):
    if i in bonus:
        T += bonus[i]
    T -= A[i]
    if T <= 0:

        # print(i)
        # print(T)

        print("No")
        break
else:
    # print(T)

    print("Yes")
