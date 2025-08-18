from collections import defaultdict

N = int(input())

# 読み込みながら連想配列を作成
dd = defaultdict(int)
for i in range(N):
    dd[input()] += 1

# 連想配列から最大値の要素のキーを取り出したリストを作成
mv = max(dd.values())
ans = [k for k, v in dd.items() if v == mv]

# 答えを表示
print(*sorted(ans), sep='\n')
