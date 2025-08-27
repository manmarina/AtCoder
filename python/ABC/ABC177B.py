S = input()
N = input()

mn = 1000
for i in range(len(S) + 1 - len(N)):
    sub = S[i:i + len(N)]
    # print(sub)
    count = 0
    for s, n in zip(sub, N):
        if s != n:
            count += 1
    if count < mn:
        mn = count
    if mn == 0:
        break
print(mn)
