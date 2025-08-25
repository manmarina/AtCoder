N = int(input())

for i in range(N // 7 + 1):
    for j in range((N - 7 * i) // 4 + 1):
        if 7 * i + 4 * j == N:
            print("Yes")
            exit()
print("No")
