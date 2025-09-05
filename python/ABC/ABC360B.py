S, T = input().split()
n, m = len(S), len(T)

for c in range(1, n):           # 1 ≤ c
    for w in range(c, n):        # c ≤ w < n
        # 取り出し位置は c-1, c-1+w, c-1+2w, ...
        # 長さが違えばスキップ（任意の枝刈り）
        k = (n - c) // w + 1
        if k != m:
            continue

        made = []
        p = c - 1
        while p < n:
            made.append(S[p])
            p += w
        if ''.join(made) == T:
            print("Yes")
            exit()
print("No")
