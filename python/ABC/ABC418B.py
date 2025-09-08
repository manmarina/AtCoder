S = input().strip()
n = len(S)

# 累積和: pref[k] = S[0:k] に含まれる 't' の個数
pref = [0] * (n + 1)
for i, ch in enumerate(S, 1):
    pref[i] = pref[i - 1] + (ch == 't')
print(pref)


best = 0.0

# 早期終了: 'ttt' があれば 1
if 'ttt' in S:
    print("1.0")
    exit()

for i in range(n):
    if S[i] != 't':
        continue
    for j in range(i + 2, n):  # 長さ>=3
        if S[j] != 't':
            continue
        num_t_inside = pref[j] - pref[i + 1]
        len_inside = j - i - 1
        rate = num_t_inside / len_inside  # 0 <= rate <= 1
        if rate > best:
            best = rate

print("{:.17f}".format(best))
