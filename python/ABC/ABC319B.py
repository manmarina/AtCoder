N = int(input())

div = [(j, N // j) for j in range(1, 9 + 1) if N % j == 0]
# print(div)

ans = []
for i in range(N + 1):
    for j, N_div_j in div:
        if i % N_div_j == 0:
            ans.append(j)
            break
    else:
        ans.append('-')
print(*ans, sep='')
