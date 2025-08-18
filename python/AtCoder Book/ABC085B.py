N = int(input())
d = [int(input()) for _ in range(N)]

# バケットを作成(setを使わない解法)
bucket = [0] * 101
for i in d:
    bucket[i] = 1
# print(bucket)

# バケットの中の1の数を合計
count = sum(bucket)

print(count)
