W, B = map(int, input().split())

w = [0]
b = [0]
S = "wbwbwwbwbwbw" * (100 // 7 + 1)
for i in range(len(S)):
    if S[i] == 'w':
        w.append(w[i] + 1)
        b.append(b[i] + 0)
    else:
        w.append(w[i] + 0)
        b.append(b[i] + 1)

# print(w)
# print(b)

for i in range(len(S) - (W + B)):
    # print(S[i:i + W + B])
    # print(w[i + W + B] - w[i])
    # print(b[i + W + B] - b[i])
    if w[i + W + B] - w[i] == W and b[i + W + B] - b[i] == B:
        print("Yes")
        break
else:
    print("No")
