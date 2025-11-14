N = int(input())
A = list(map(int, input().split()))

ans = 0

for l in range(N):
    x = A[l]  # 最小値
    for r in range(l, N):  # l,r を全探索
        x = min(x, A[r])  # 最小値を更新
        ans = max(ans, x * (r - l + 1))  # 食べた個数が最大であれば更新

print(ans)

"""
工夫して探索の通り数を減らす全探索
公式解説
l を固定して r を右へ伸ばすと、区間の最小値は単調に減るか、同じ。
つまりx = min(A_l ... A_r)を A_r を追加しながら更新できる。
これは O(1) で更新できる！

https://atcoder.jp/contests/abc189/tasks/abc189_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69172a7a-ad08-8323-9e75-c3536b12f8b4
"""
