N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
# print(A)
ans = []
for a in A:
    if K > 0:
        div, mod = divmod(a, X)
        if div < K:
            ans.append(mod)
            K -= div
        else:
            ans.append(a - K * X)
            K = 0
    else:  # この処理が抜けていた
        ans.append(a)
# print(ans)
# print(sum(ans))
# print(K)

ans.sort(reverse=True)
# print(ans)
for i, a in enumerate(ans):
    if K > 0:
        ans[i] = 0
        K -= 1
# print(ans)
print(sum(ans))

"""
貪欲法（Greedy）+ソート
チャッピーの助言でAC

クーポン1枚で「好きなAiからXを引く（負にならない）」。
合計K枚で配列の総和を最小にしたい。

https://atcoder.jp/contests/abc246/submissions/69770080
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68dd347d-1d94-832d-8fcc-d5303aca53b1
"""
