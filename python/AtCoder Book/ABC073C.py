from collections import defaultdict

N = int(input())

# 入力を連想配列に格納
dd = defaultdict(int)
for i in range(N):
    a = int(input())
    if dd[a] == 0:
        dd[a] = 1
    else:
        dd[a] = 0

# 答えを表示
# print(dd)
print(sum(v for v in dd.values()))
