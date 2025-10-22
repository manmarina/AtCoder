N = int(input())
q, r = [], []
for _ in range(N):
    qi, ri = map(int, input().split())
    q.append(qi)
    r.append(ri)

Q = int(input())
td = [list(map(int, input().split())) for _ in range(Q)]

for t, d in td:  # d=ゴミを出した日
    t -= 1  # 0-indexed i種類のゴミ

    ri = r[t]  # i種類目のゴミのr
    qi = q[t]  # i種類目のゴミのq

    temp = d % qi  # 問題文の条件 この値がriなら収集日

    # 次の収集日までの日数deltaを求めたい
    if temp <= ri:  # ri以下なら
        delta = ri - temp  # 単純に引けば良い
    else:  # riよりも大きいときはマイナスにならないように
        delta = ri + qi - temp  # riに次の周期を足してから引けば良い

    print(d + delta)

"""
シミュレーション系
自力解

チャッピーも解説放送も理解できなかったので自分で考えた
https://atcoder.jp/contests/abc378/tasks/abc378_b
https://chatgpt.com/c/68bb7d5c-fdc8-832a-a649-3fb32226f5f3 <- 参考にしなくても大丈夫
"""
