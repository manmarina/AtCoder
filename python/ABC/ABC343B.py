N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for row in A:
    temp = []
    for i, c in enumerate(row):
        if c == 1:
            temp.append(i + 1)
    print(*temp)
