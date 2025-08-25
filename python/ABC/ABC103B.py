S = input()
T = input()

for i in range(len(S)):
    rot = S[i:] + S[:i]
    if T == rot:
        print("Yes")
        break
else:
    print("No")
