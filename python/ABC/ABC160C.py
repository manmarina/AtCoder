K, N = map(int, input().split())
A = list(map(int, input().split()))

mx = A[0] + K - A[-1]  # 最初の家を最後の家の距離を初期値とする
for i in range(N - 1):  # その他すべての家の間の距離を見る
    mx = max(mx, A[i + 1] - A[i])  # 最大値なら更新する
print(K - mx)  # 1周の距離から最大値を引いたものが答え

"""
基本実装問題
家の間の距離が最も長いところを避けるルートを選択する。

https://atcoder.jp/contests/abc160/tasks/abc160_c
"""
