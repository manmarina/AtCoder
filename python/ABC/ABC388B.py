N, D = map(int, input().split())
TL = [list(map(int, input().split()))for _ in range(N)]

ans = []
for i in range(1, D + 1):
    temp = []
    for t, l in TL:
        temp.append(t * (l + i))
    ans.append(max(temp))
print(*ans, sep='\n')
