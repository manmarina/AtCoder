N = int(input())
P = list(map(int, input().split()))

# 値→ランクの辞書を作る
vals = sorted(P, reverse=True)
rank_of = {}
for i, v in enumerate(vals, 1):
    if v not in rank_of:
        rank_of[v] = i
print(rank_of)

# インデックス順に値→ランクを取り出して出力
for x in P:
    print(rank_of[x])
