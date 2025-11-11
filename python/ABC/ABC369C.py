N = int(input())
A = list(map(int, input().split()))


def check(l, r):
    # 区間 [l, r) が条件を満たすかを判定
    if r - l <= 2:  # 長さ2以下なら常にOK
        return True
    # 長さ3以上の場合、最後の3つが等差であるかどうかを比較
    return A[r - 1] - A[r - 2] == A[r - 2] - A[r - 3]


res = 0
right = 0
for left in range(N):  # すべてのleftについて
    if right < left:
        right = left
    while right < N and check(left, right + 1):  # right + 1がokなら
        right += 1  # right + 1にする
    res += right - left  # あるleftでの階差数列の個数を足す

print(res)

"""
しゃくとり法
とても教育的で典型的なしゃくとり法の問題！
まだ理解不十分。。

けんちょん
https://drken1215.hatenablog.com/entry/2024/09/01/153129

https://atcoder.jp/contests/abc369/tasks/abc369_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6912e5bf-e608-8321-b398-34bb631ba0bb
"""
