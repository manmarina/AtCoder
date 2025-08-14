N = int(input())
H = list(map(int, input().split()))

peak = H[0]
count = 1
for i in range(1, N):
    if peak <= H[i]:
        count += 1
        peak = H[i]

print(count)
