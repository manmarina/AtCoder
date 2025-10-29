N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

minT = min(T)
start = T.index(minT)  # 最初に宝石を貰う人のインデックス
ans = [minT]

for i in range(1, N):
    pre = (start + i - 1) % N  # curの一つ前の人
    cur = (start + i) % N  # start+1から開始して、円環距離で最後まで
    ans.append(min(T[cur], ans[i - 1] + S[pre]))  # 高橋くんがくれる時間と、前の人がくれる時間の早い方
# print(ans)

for i in range(N):
    idx = (N - start + i) % N  # index0の位置を求める
    print(ans[idx])

"""
円環距離（サイクル距離）

最初に宝石を貰う人からスタート。
次の人は、前の人からもらうか、高橋くんからもらうか早い方。これを円環距離を利用して繰り返す。
結果の出力も、index0から出力したいので、円環距離を使用してindex0の位置を求めている。

https://atcoder.jp/contests/abc214/tasks/abc214_c
"""
