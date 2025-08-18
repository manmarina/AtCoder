from collections import defaultdict

N = int(input())

# 入力を直接連想配列に格納
dd = defaultdict(int)
for a in map(int, input().split()):
    dd[a] += 1
# print(dd)

# 連想配列を走査して、削除すべき要素の数をカウント
count = 0
for k, v in dd.items():
    if k == v:
        continue
    elif k < v:
        count += v - k
    else:
        count += v
print(count)
