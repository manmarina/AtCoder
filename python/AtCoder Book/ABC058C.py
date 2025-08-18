from collections import defaultdict

N = int(input())

# 入力の都度リストに連想配列を追加
LS = []
for i in range(N):
    S = input()
    dd = defaultdict(int)
    for s in S:
        dd[s] += 1
    LS.append(dd)
# print(LS)

# 共通部分を求めリストに追加
ans = []
for k in LS[0]:
    if all(k in d for d in LS[1:]):
        count = min(d[k] for d in LS)
        ans.extend([k] * count)
# print(ans)

# 辞書順に並べる
ans.sort()

# 文字列化
print(*ans, sep='')
