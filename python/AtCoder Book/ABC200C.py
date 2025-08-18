from collections import defaultdict

N = int(input())

# 入力の都度、200の剰余を計算して連想配列に追加
dd = defaultdict(int)
for a in map(int, input().split()):
    dd[a % 200] += 1
# print(dd)

# 正解を計算
ans = sum(v * (v - 1) // 2 for v in dd.values())
print(ans)
