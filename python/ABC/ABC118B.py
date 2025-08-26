N, M = map(int, input().split())
KA = [list(map(int, input().split())) for i in range(N)]

# print(KA)

bucket = [0] * (M + 1)
for row in KA:
    for i in range(1, row[0] + 1):
        bucket[row[i]] += 1

# print(bucket)

print(bucket.count(N))
