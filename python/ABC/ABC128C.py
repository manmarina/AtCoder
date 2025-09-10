N, M = map(int, input().split())
s = []
for _ in range(M):
    temp = list(map(int, input().split()))
    temp.pop(0)
    s.append(temp)
p = list(map(int, input().split()))
# print(s)

# 電球ごとの接続スイッチをビットマスク化
masks = []
for switches in s:
    mask = 0
    for x in switches:
        mask |= 1 << (x - 1)  # 1-index -> 0-index
    masks.append(mask)
# print(masks)

# ビットマスクのスイッチパターンを電球ごとに試して、点灯しなければパス 全ての電球が点灯したらans++
ans = 0
for mask in range(1 << N):  # スイッチ割り当て
    for j in range(M):  # 電球のスイッチと、ビットマスクのスイッチパターンを照合
        # if ((mask & masks[j]).bit_count() % 2) != p[j]:
        if (bin(mask & masks[j]).count('1') % 2) != p[j]:  # 古いpythonならこちら
            break
    else:
        ans += 1

print(ans)
