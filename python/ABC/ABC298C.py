from collections import defaultdict

N = int(input())
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

box = defaultdict(list)
card = defaultdict(set)

for q in Query:
    if q[0] == 1:
        _, i, j = q
        box[j].append(i)
        card[i].add(j)
    elif q[0] == 2:
        _, i = q
        print(*sorted(box[i]))
    else:  # q[0] == 3:
        _, i = q
        print(*sorted(card[i]))


"""
クエリ処理
箱にカードを入れ、箱に入っているカードや、カードを入れた箱を答える。
出力するべき数はすべてのクエリ合計で2x10^5個以下なので、ソートの計算量に関して特に考えずにACできた。
(ソートの計算量はO(N log N) -> すべてのクエリのソート合計で3.5 x 10^6 程度に収まる。)

けんちょんの解説
https://drken1215.hatenablog.com/entry/2023/04/17/235600

https://atcoder.jp/contests/abc298/tasks/abc298_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691ddeb7-0a38-8321-b17b-cad72f649579
"""
