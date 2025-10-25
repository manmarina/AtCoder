N, M = map(int, input().split())
B = [input().split() for _ in range(N)]
# print(B)

# # 正解となる行列の確認
# for i in range(1, 10 + 1):
#     for j in range(1, 7 + 1):
#         print((i - 1) * 7 + j, end=' ')
#     print()

# 先頭数値の周期性確認
head = int(B[0][0])
if M == 1:
    if not (0 <= head % 7 <= 6):
        print("No")
        exit()
else:
    if not (1 <= head % 7 <= 8 - M):
        print("No")
        exit()

# 列チェック
for i in range(1, N):
    pre = int(B[i - 1][0])
    cur = int(B[i][0])
    if cur != pre + 7:
        print("No")
        exit()

# 行チェック
for j in range(1, M):
    pre = int(B[0][j - 1])
    cur = int(B[0][j])
    if cur != pre + 1:
        print("No")
        exit()

print("Yes")

"""
数学的な気づき系
回答済みであることに気づかずリトライ
カレンダーの周期性が当てはまるかの確認

https://atcoder.jp/contests/abc225/tasks/abc225_c
"""
