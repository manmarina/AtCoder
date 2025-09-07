S = input()

ls = len(S)
count = 0
for i in range((ls - 3) // 2 + 1):
    lt = 3 + i * 2
    for j in range(ls - lt + 1):
        a = j
        b = j + i + 1
        c = j + 2 * i + 2
        if S[a] == 'A' and S[b] == 'B' and S[c] == 'C':
            count += 1
print(count)
