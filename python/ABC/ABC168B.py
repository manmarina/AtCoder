K = int(input())
S = input()

if len(S) > K:
    st = S[:K]
    st += "..."
else:
    st = S

print(st)
