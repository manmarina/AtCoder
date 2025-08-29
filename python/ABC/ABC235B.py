N = int(input())
H = list(map(int, input().split()))

for i in range(1, N):
    if H[i - 1] >= H[i]:
        print(H[i - 1])
        break
else:
    print(H[i])
