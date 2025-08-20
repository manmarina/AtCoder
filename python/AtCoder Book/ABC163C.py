N = int(input())
A = list(map(int, input().split()))

# 子リスト（部下リスト）
children = [[] for _ in range(N)]

# 社員 2..N の上司が A[i] なので辺を張る
for i, boss in enumerate(A, start=2):  # i=社員番号
    children[boss - 1].append(i - 1)       # boss, i は 0-index に変換

# 部下人数を数える
for i in range(N):
    print(len(children[i]))

# print(children)
