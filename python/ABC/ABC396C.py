N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

# 黒、白の配列を降順にソート
B.sort(reverse=True)
W.sort(reverse=True)
# print("B:", B)
# print("W:", W)

# 黒を加算する
Bt = 0
i = 0
if B[0] >= 0:  # 黒の最初が正なら
    for i in range(N):  # 最後まで見る
        if B[i] >= 0:
            Bt += B[i]
        else:
            i -= 1  # iを一つ戻す
            break
# print("Bt:", Bt, "i:", i)

# 白を加算する
Wt = 0
j = 0
if B[0] >= 0:  # 黒の最初が正なら
    for j in range(min(M, i + 1)):  # 最後か、iの小さい方までみる
        if W[j] >= 0:
            Wt += W[j]
        else:
            j -= 1  # jを一つ戻す
            break
# print("Wt:", Wt, "j:", j)

# バグ対策　黒の最初が正なら
if B[0] >= 0:
    i += 1
    j += 1

# 最後に達するか、黒と白の合計が正の間繰り返す
while i < N and j < M and W[j] + B[i] >= 0:
    Bt += B[i]
    Wt += W[j]
    i += 1
    j += 1
# print("Bt:", Bt, "i:", i)
# print("Wt:", Wt, "j:", j)

print(Bt + Wt)

"""
場合分け系
どの解説もわからなかったので自分のロジックを長時間かけてAC
テストケースをたくさん作り、異常値が出たらデバッグを繰り返した

https://atcoder.jp/contests/abc396/tasks/abc396_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68fc381e-ce74-8324-9985-7d56e3b90d3b
"""
