N, M = map(int, input().split())

# 電球ごとの接続スイッチをビットマスク化
masks = []
for _ in range(M):
    data = list(map(int, input().split()))
    k, arr = data[0], data[1:]
    mask = 0
    for x in arr:
        mask |= 1 << (x - 1)   # 1-index -> 0-index
    masks.append(mask)

p = list(map(int, input().split()))

ans = 0
for s in range(1 << N):           # スイッチ割り当て
    ok = True
    for j in range(M):
        # if ((s & masks[j]).bit_count() % 2) != p[j]:
        if (bin(s & masks[j]).count('1') % 2) != p[j]:  # 古いバージョンのpythonならこちら
            ok = False
            break
    if ok:
        ans += 1
print(ans)
