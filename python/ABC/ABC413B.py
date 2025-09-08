N = int(input())
S = [input().strip() for _ in range(N)]

seen = set()
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        seen.add(S[i] + S[j])

print(len(seen))
