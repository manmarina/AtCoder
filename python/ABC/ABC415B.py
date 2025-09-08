S = input()

ans = []
for i, s in enumerate(S, 1):
    if s == '#':
        ans.append(i)
# print(ans)

for i in range(0, len(ans), 2):
    print(f"{ans[i]},{ans[i+1]}")
