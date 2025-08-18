N, M = map(int, input().split())

# 空のバケットを作成
bucket = [0] * 31

# スキャンしながらバケットに追加
for i in range(N):
    A = (list(map(int, input().split())))
    for a in A[1:]:
        bucket[a] += 1

# バケットを走査して、カウントがNのものの数を表示
count = 0
for i in bucket:
    if i == N:
        count += 1
print(count)
