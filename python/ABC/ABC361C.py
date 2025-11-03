N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(A)

ans = 10**9
for i in range(N - (N - K) + 1):  # iをずらしながら、K+1パターン試す
    # print('i:', i, 'i+N-K-1：', i + N - K - 1)　# i=最小値のインデックス,i+N-K-1=最大値のインデックス
    # print(A[i], A[i + N - K - 1])
    ans = min(ans, A[i + N - K - 1] - A[i])  # 最大値 - 最小値
print(ans)

"""
工夫して探索の通り数を減らす「全探索 + 枝刈り」
削除パターンをすべて試すとTLE。
削除するのは最大値付近x個と、最小値付近K-x個の合計K個。
つまりx=0~K個(2*10^5)の範囲を探索すればよいので、これなら計算可能。
最初にソートしておくので、min,maxの取得も含め、各探索はO(1)で計算できる。

けんちょんの解説
https://atcoder.jp/contests/abc361/tasks/abc361_c

https://atcoder.jp/contests/abc361/tasks/abc361_c
"""
