S = input()
N = len(S)

# ランレングス圧縮
lens = []
i = 0
while i < N:
    j = i
    while j < N and S[j] == S[i]:
        j += 1
    lens.append((int(S[i]), j - i))  # (文字,文字長)を記録
    i = j
# print(lens)

cnt = 0
for i in range(len(lens) - 1):
    if lens[i][0] + 1 == lens[i + 1][0]:
        cnt += min(lens[i][1], lens[i + 1][1])
print(cnt)

"""
ランレングス圧縮
テンプレートを活用。

https://atcoder.jp/contests/abc433/tasks/abc433_c
"""
