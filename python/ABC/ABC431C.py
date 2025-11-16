N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()
# print(H)
# print(B)

cnt = 0  # 倒れないロボットの数
k = 0
for i in range(N):  # H[i]~H[N-1]まで
    while i + k < M and H[i] > B[i + k]:  # 頭が体より重い間はkを増やす
        k += 1
    if i + k >= M:
        break
    # head = H[i]
    # body = B[i + k]
    cnt += 1
# print(k)
# print(cnt)
if cnt >= K:  # 倒れないロボットがKより多くできた時
    print("Yes")
else:
    print("No")

"""
シミュレーション
頭も体も小さい方から組み合わせしてゆく。
組み合わせて倒れてしまうときは、次の体を試すのを最後まで繰り返す。
公式解説のように、頭の小さい方からK個、体の大きい方からK個を組み合わせて考えたほうが簡単そう。

https://atcoder.jp/contests/abc431/tasks/abc431_c
"""
