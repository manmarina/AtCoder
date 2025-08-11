import sys

N = int(input())
S = []
for i in range(N):
    S.append(input())

check1 = "HDCS"
check2 = "A23456789TJQK"

if len(S) != len(set(S)):
    print("No")
    sys.exit()

for i in range(N):
    if S[i][0] not in check1:
        print("No")
        sys.exit()
    if S[i][1] not in check2:
        print("No")
        sys.exit()

print("Yes")
