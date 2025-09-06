S = input()

run = 0
ans = []
for s in S:
    if s == '-':
        run += 1
    else:
        if run:
            ans.append(run)
        run = 0
print(*ans)
