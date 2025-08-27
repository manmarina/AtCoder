N = int(input())
S = input()

if len(S) % 2:
    print("No")
    exit()

cen = len(S) // 2
L = S[:cen]
R = S[cen:]

if L == R:
    print("Yes")
else:
    print("No")
