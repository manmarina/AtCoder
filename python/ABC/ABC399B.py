N = int(input())
P = list(map(int, input().split()))

# インデックスと点数のタプルのリストを作り、点数の逆順でソート
P = [(i, p) for i, p in enumerate(P, 1)]
P.sort(key=lambda x: (-x[1], x[0]))
# print(P)

# インデックスと順位のタプルのリストを作成
rank = 1
count = 0
ans = [(P[0][0], 1)]
pre = P[0][1]
for i in range(1, N):
    if P[i][1] == pre:
        count += 1
        ans.append((P[i][0], rank))
    else:
        rank = rank + 1 + count
        count = 0
        ans.append((P[i][0], rank))
        pre = P[i][1]
# print(ans)

# インデックス順でソートして順位を出力
ans.sort(key=lambda x: x[0])
# print(ans)
for i in range(N):
    print(ans[i][1])
