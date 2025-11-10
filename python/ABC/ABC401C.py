N, K = map(int, input().split())

sum_ = K
A = [1] * K
# print(A)

for i in range(K, N + 1):
    A.append(sum_)
    # sum_を更新する(今回分を足す & K個前を引く)
    sum_ = (sum_ + A[i] - A[i - K]) % 10**9

print(A[-1])  # 最後の要素が答え

"""
計算量を削減したシミュレーション
リトライ

解説
https://atcoder.jp/contests/abc401/editorial/12689
愚直に毎回 Aiを求めると O(NK) かかってしまい実行時間制限に間に合いません。
ここで、Sをデータとして保持することにして、S を適宜更新することを考えます。

https://atcoder.jp/contests/abc401/tasks/abc401_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69042c33-f098-8323-a7d9-bc1ce4bfe36e
"""
