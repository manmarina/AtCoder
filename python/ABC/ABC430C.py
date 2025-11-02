from bisect import bisect_left


N, A, B = map(int, input().split())
S = input()

# aとbの累積和配列を作成
Xa = [0]
Xb = [0]
for i in range(N):
    if S[i] == 'a':
        Xa.append(Xa[i] + 1)
        Xb.append(Xb[i])
    else:  # S[i] == 'b':
        Xa.append(Xa[i])
        Xb.append(Xb[i] + 1)
# print("Xa", Xa)
# print("Xb", Xb)

ans = []
for i in range(N - A):
    na = A + Xa[i]
    nb = B + Xb[i]
    # print("na:", na, "nb:", nb)
    Ra = bisect_left(Xa, na)
    Rb = bisect_left(Xb, nb)
    # print("Ra:", Ra, "Rb:", Rb)
    if Ra <= Rb - 1:
        ans.append(Rb - Ra)
# print(ans)
print(sum(ans))

"""
累積和 + 二分探索
解説
https://atcoder.jp/contests/abc430/editorial/14299
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69069477-39b8-8322-84d8-25a65021538d

https://atcoder.jp/contests/abc430/tasks/abc430_c
"""
