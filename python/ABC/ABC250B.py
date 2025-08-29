N, A, B = map(int, input().split())

# 1ブロック行（= 横に N 個のブロックが並ぶ）のテンプレを2種類作る
row_even = []  # 偶数ブロック行: .ブロックから開始
row_odd = []  # 奇数ブロック行: #ブロックから開始

dot_block = '.' * B
hash_block = '#' * B

for c in range(N):
    if c % 2 == 0:
        row_even.append(dot_block)
        row_odd.append(hash_block)
    else:
        row_even.append(hash_block)
        row_odd.append(dot_block)

row_even = ''.join(row_even)
row_odd = ''.join(row_odd)

# ブロック行ごとに A 行ずつ出力
for r in range(N):
    line = row_even if r % 2 == 0 else row_odd
    for _ in range(A):
        print(line)
