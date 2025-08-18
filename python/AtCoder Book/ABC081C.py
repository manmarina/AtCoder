from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

# Aから連想配列を作成
dd = defaultdict(int)
for a in A:
    dd[a] += 1

# Kと連想配列の要素数を比較
if len(dd) < K:
    print(0)
else:
    sv = sorted(dd.values())
    # print(sv)
    dk = len(dd) - K  # 書き換えが必要な種類数
    print(sum(v for v in sv[:dk]))
