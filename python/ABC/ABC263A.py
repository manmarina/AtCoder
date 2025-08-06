S = list(map(int, input().split()))
S.sort()

count = 1
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1

if count == 2:
    print("Yes")
else:
    print("No")
