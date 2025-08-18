from collections import defaultdict

N, M = map(int, input().split())

# スキャンしながら連想配列に追加
dd = defaultdict(int)
for i in range(N):
    A = (list(map(int, input().split())))
    for a in A[1:]:
        dd[a] += 1

# 連想配列を走査して、カウントがNのものの数を表示
count = 0
for i in dd.values():
    if i == N:
        count += 1
print(count)
