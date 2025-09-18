N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):  # CとAを別のリストに格納
    temp = list(map(int, input().split()))
    c, *a = temp
    C.append(c)
    A.append(a)
# print(C)
# print(A)

# ビットマスクで購入する書籍の全パターンを網羅　各購入パターンの金額と理解度をansに格納
ans = []
for mask in range(1 << N):
    cost = 0
    level = [0] * M
    for i in range(N):
        if (mask >> i) & 1:
            cost += C[i]
            for j in range(M):
                level[j] += A[i][j]
    ans.append((cost, level))

# 金額順にソートしたリストの理解度をXと照合
# 理解度がすべてXを超えていたら金額を表示して終了
# 理解度がすべてXを超えるパターンがなければ-1を表示して終了
ans.sort(key=lambda x: x[0])
# print(ans)

for cost, level in ans:
    if all(l >= X for l in level):
        print(cost)
        break
else:
    print(-1)

"""
自力で解けたビット全探索
bit全探索（部分集合列挙）

本の数 N ≤ 15 なので、全部の選び方は 2^N（最大 32768）。余裕で全列挙できます。
各 subset（mask）について、
    合計コスト cost を加算
    各アルゴリズム力 skill[j]（j=0..M-1）を加算
    全ての skill[j] ≥ X を満たすか判定
"""
