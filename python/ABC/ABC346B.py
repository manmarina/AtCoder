W, B = map(int, input().split())

S = "wbwbwwbwbwbw" * (100 // 7 + 1)

for i in range(12):
    chk = S[i:i + W + B]
    wc = chk.count('w')
    bc = chk.count('b')

    if wc == W and bc == B:
        print("Yes")
        break
else:
    print("No")
