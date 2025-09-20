from collections import defaultdict


n = int(input())
S = [input() for _ in range(n)]

# 文字列ごとにdefaultdictを作成してlistに格納
ddl = []
for word in S:
    temp = defaultdict(int)
    for w in word:
        temp[w] += 1
    ddl.append(temp)
# print(ddl)

ans = []
for k in ddl[0]:  # 最初の文字列のddのキーで検索
    if all(k in dd for dd in ddl[1:]):  # 全ての文字列のddにキーが含まれていたら
        mn = min(dd[k] for dd in ddl)  # 一番少ない数を検索してmnに格納
        ans.extend(k * mn)  # キーをmn個格納 (append ではなく extendなのがポイント)
# print(ans)

ans.sort()
print(*ans, sep='')

"""
連想配列
AtCoder本で解いたときのコードを参照

文字列ごとにddを作成してddlに格納
ddlの最初のddのキーを全てのddで検索
すべてに含まれていたら、
要素の最小値を取得
ansにキーを要素の最小値個格納する（extend）
"""
