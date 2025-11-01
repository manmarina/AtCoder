N = int(input())
X = list(map(int, input().split()))

ans = []
for p in range(min(X), max(X)+1):  # pの探索範囲はmin(X) ~ max(X)
    loss = 0
    for i in range(N):
        loss += (X[i] - p)**2
    ans.append(loss)
# print(ans)
print(min(ans))

"""
問題文の理解が難解系
チャッピー
pの探索範囲がわかりにくい。
P の取りうる範囲は、最小値を求める観点では [min(X), max(X)] で十分。

https://atcoder.jp/contests/abc156/tasks/abc156_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6905b8c8-d4c8-8322-b503-367c218addb9
"""
