N, Q = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(Q)]
# print(query)

hole = [[i] for i in range(N + 1)]  # 巣 -> 鳩
# print(hole)
pigeon = [i for i in range(N + 1)]  # 鳩 -> 巣
# print(pigeon)

multi = 0  # 複数の鳩がいる巣の数
for q in query:
    if q[0] == 1:
        _, p, h = q
        hole[pigeon[p]].remove(p)  # 前の巣から鳩を削除
        if len(hole[pigeon[p]]) == 1:  # 鳩の数が1になったら
            multi -= 1  # 複数の鳩がいる巣の数を減らす

        hole[h].append(p)  # 次の巣に鳩を追加
        if len(hole[h]) == 2:  # 鳩の数が2になったら
            multi += 1  # 複数の鳩がいる巣の数を増やす

        pigeon[p] = h  # 鳩を次の巣に移動する
        # print("hole:", hole)
        # print("pigeon:", pigeon)

    else:  # q[0] == 2:
        print(multi)  # 複数の鳩がいる巣の数を出力する

"""
計算量を削減したクエリ処理 + バケット
O(1)で検索できるように、holeとpigeonの2つの配列を用意する。
鳩が移動する度に、複数の鳩がいる巣の数をカウントしておく。

https://atcoder.jp/contests/abc391/tasks/abc391_c
"""
