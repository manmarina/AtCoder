S = input().strip()
T = input().strip()

m = min(len(S), len(T))
for i in range(m):
    if S[i] != T[i]:
        print(i + 1)
        break
else:
    # 先頭 m 文字が一致
    if len(S) == len(T):
        print(0)
    else:
        print(m + 1)
