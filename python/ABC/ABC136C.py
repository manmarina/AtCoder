N = int(input())
H = list(map(int, input().split()))

H[0] -= 1  # 先頭は-1しておく
for i in range(1, N):
    if H[i] - H[i - 1] >= 1:  # 一つ前とくらべ1以上高ければ
        H[i] -= 1  # 一つ低くする
    if H[i - 1] > H[i]:  # 一つ前のほうが高ければ終了
        print("No")
        exit()
print("Yes")

"""
シミュレーション系
O(N)
https://atcoder.jp/contests/abc136/tasks/abc136_c
"""
