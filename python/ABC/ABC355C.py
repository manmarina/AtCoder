N, T = map(int, input().split())
A = list(map(int, input().split()))

grid = [[0] * N for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        grid[i - 1][j - 1] = N * (i - 1) + j
# print(grid)

bingo = set()
# bingo横ライン
for row in grid:
    bingo.add(frozenset(row))  # setに格納するためにfrozensetにする

# bingo縦ライン
for j in range(N):
    bingo.add(frozenset(grid[i][j] for i in range(N)))

# bingo斜め（左上→右下）
bingo.add(frozenset(grid[i][i] for i in range(N)))

# bingo斜め（右上→左下）
bingo.add(frozenset(grid[N - 1 - i][i] for i in range(N)))
# print(bingo)

# ### ここが重い ###
# bingoチェック
for i in range(N, T + 1):  # N以上からチェック開始
    turn = set(A[:i])
    # print(turn)

    for b in bingo:  # bingoセットからbingoパターンを取り出す
        # print(b)
        if b <= turn:  # turnの中にbingoパターンを発見したら
            print(i)  # 抽選回数を表示
            exit()
# ### ここまでが重い ###

# bingoしなかったとき
print("-1")

"""
TLE
チャッピーの見積もりで、全体の計算量はO(N^2 + T^2 + T·N^2)
Tは最大2x10^5なので、全然間に合わない。

https://atcoder.jp/contests/abc355/tasks/abc355_c
https://chatgpt.com/c/68fb2c1f-c294-8323-beed-4683776be355
"""
