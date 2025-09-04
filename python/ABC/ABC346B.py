W, B = map(int, input().split())

pat = "wbwbwwbwbwbw"
need = W + B
S = pat * (need // len(pat) + 3)
print(S)

# w の累積和
pre_w = [0]
for ch in S:
    pre_w.append(pre_w[-1] + (ch == 'w'))

ok = False
for start in range(len(pat)):           # 開始位置は周期12通りだけ試せばよい
    end = start + need
    wcnt = pre_w[end] - pre_w[start]
    bcnt = need - wcnt
    if wcnt == W and bcnt == B:
        ok = True
        break

print("Yes" if ok else "No")
