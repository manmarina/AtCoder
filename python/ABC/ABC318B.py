N = int(input())

ABCD = []
for i in range(N):
    ABCD.append(list(map(int, input().split())))

count = 0
for x in range(100):
    for y in range(100):
        for A, B, C, D in ABCD:
            if A <= x < B and C <= y < D:
                count += 1
                break

print(count)
