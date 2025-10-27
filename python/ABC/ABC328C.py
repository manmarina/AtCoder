# 入力
N, Q = map(int, input().split())
S = input()
print(S)

# 累積和を準備
# S[i] == S[i+1] なら 1 を加算して累積
sum_list = [0] * N
for i in range(N - 1):
    sum_list[i + 1] = sum_list[i] + (S[i] == S[i + 1])
print(sum_list)


# クエリ処理
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1  # 0-indexed に
    r -= 1  # 区間 [l,r+1) を考えるのではなく、区間 [l,r) を考える
    print(sum_list[r] - sum_list[l])

"""
累積和
けんちょん
https://drken1215.hatenablog.com/entry/2023/11/12/192606
122Cと同じように解ける。

https://atcoder.jp/contests/abc122/tasks/abc122_c
"""
