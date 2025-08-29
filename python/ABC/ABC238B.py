N = int(input())
A = list(map(int, input().split()))

cuts = [0]
cur = 0
for a in A:
    cur = (cur + a) % 360
    cuts.append(cur)
cuts.append(360)
cuts.sort()

# print(cuts)

ans = 0
for i in range(len(cuts) - 1):
    deg = cuts[i + 1] - cuts[i]
    ans = max(ans, deg)
print(ans)
