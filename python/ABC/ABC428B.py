N, K = map(int, input().split())
S = input()

seen = set()
ans = []
for i in range(N + 1 - K):
    # print(i)
    s = S[i:i + K]
    # print(s)
    if s in seen:
        continue

    count = 0
    seen.add(s)
    for i in range(N + 1 - K):
        if s == S[i:i + K]:
            count += 1
    else:
        ans.append((s, count))

# print(seen)
# print(ans)
mx = max(a[1] for a in ans)
print(mx)

sect = []
for a in ans:
    if a[1] == mx:
        sect.append(a[0])
print(*sorted(sect))
