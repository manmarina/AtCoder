from collections import defaultdict

N = int(input())

# inputしながら連想配列に追加してカウント
S = defaultdict(int)
for i in range(N):
    s = ''.join(sorted(input()))
    S[s] += 1

# 連想配列のカウントから組み合わせを計算して合算
total = sum(v * (v - 1) // 2 for v in S.values())
print(total)
