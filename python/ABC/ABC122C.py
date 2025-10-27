# 入力
N, Q = map(int, input().split())
s = input()
# print(s)

# 累積和の準備
acc = [0] * (N + 1)
for i in range(1, N + 1):
    if i < N and s[i - 1] == 'A' and s[i] == 'C':  # 'A'かつ右隣が'C'のとき
        acc[i] = acc[i - 1] + 1
    else:
        acc[i] = acc[i - 1]
# print(acc)

# クエリ処理
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    # "TTACTTTA | C" のような「右端の 'A' の右隣に 'C' がある」というような 'A' を除外するため
    r -= 1  # 区間 [l,r+1) を考えるのではなく、区間 [l,r) を考える
    print(acc[r] - acc[l])

"""
累積和
けんちょん
https://drken1215.hatenablog.com/entry/2023/11/12/192606
区間 [l,r+1) を考えるのではなく、区間 [l,r) を考える。
"TTACTTTA | C" のような「右端の 'A' の右隣に 'C' がある」というような 'A' を除外するため。

https://atcoder.jp/contests/abc122/tasks/abc122_c
"""
