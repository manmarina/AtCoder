S = input().strip()
K = int(input())

# すべて同じ文字なら一塊になるので、長さ(K*len)の ⌊/2⌋
if S == S[0] * len(S):
    print((len(S) * K) // 2)
    exit()

# 連長（run-length）を作る
runs = []
i, n = 0, len(S)
while i < n:
    j = i
    while j < n and S[j] == S[i]:
        j += 1
    runs.append(j - i)   # 連続長
    i = j

# 1 本あたりの「同文字ペア数」= Σ⌊len/2⌋
base = sum(l // 2 for l in runs)

# 先頭と末尾の文字が違うなら、各コピーは独立 → K 倍するだけ
if S[0] != S[-1]:
    print(base * K)
else:
    # 同じなら、境界で最後の連長と最初の連長がくっつく。
    a = runs[0]
    b = runs[-1]
    # 1 つの境界で増える分:
    # ⌊(a+b)/2⌋ - ⌊a/2⌋ - ⌊b/2⌋
    delta = (a + b) // 2 - (a // 2) - (b // 2)
    ans = base * K + (K - 1) * delta
    print(ans)
