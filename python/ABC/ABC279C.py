H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]
# print(S)
# print(T)

Sb = []
for j in range(W):
    temp = 0
    for i in range(H):
        if S[i][j] == '#':
            temp = temp * 2 + 1
        else:
            temp *= 2
    Sb.append(temp)
Sb.sort()
# print(Sb)

Tb = []
for j in range(W):
    temp = 0
    for i in range(H):
        if T[i][j] == '#':
            temp = temp * 2 + 1
        else:
            temp *= 2
    Tb.append(temp)
Tb.sort()
# print(Tb)

for i in range(W):
    if Sb[i] != Tb[i]:
        print("No")
        exit()
print("Yes")

"""
TLE

https://atcoder.jp/contests/abc279/tasks/abc279_c
"""
