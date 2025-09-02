p, q = input().split()

# 隣接距離
d = [3, 1, 4, 1, 5, 9]

# 累積和で各点の「座標」を作る（A=0基準）
pos = [0]
for x in d:
    pos.append(pos[-1] + x)
print(pos)

i = ord(p) - ord('A')  # A->0, B->1, ..., G->6
j = ord(q) - ord('A')

print(abs(pos[i] - pos[j]))
